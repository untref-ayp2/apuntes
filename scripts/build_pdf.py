import argparse
import os
import re
import shutil
import subprocess
import sys

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
SOURCE_DIR = os.path.join(PROJECT_ROOT, "contenidos")
TEMP_DIR = os.path.join(PROJECT_ROOT, "contenidos/_build/pdf_temp")
EXPORTS_DIR = os.path.join(PROJECT_ROOT, "contenidos/exports")


def setup_temp_dir():
    """Creates a clean temporary directory and copies content."""
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)

    print(f"Copying {SOURCE_DIR} to {TEMP_DIR}...")
    shutil.copytree(SOURCE_DIR, TEMP_DIR, ignore=shutil.ignore_patterns("_build", "exports"))


def fix_line_for_typst(line):
    """Fix LaTeX math syntax that Typst doesn't support."""
    # Replace \left\lfloor ... \right\rfloor with floor(...)
    line = re.sub(r"\\left\\lfloor\s*(.*?)\s*\\right\\rfloor", r"floor(\1)", line)
    # Replace \lfloor ... \rfloor
    line = re.sub(r"\\lfloor\s*(.*?)\s*\\rfloor", r"floor(\1)", line)
    # Replace standalone \lfloor / \rfloor
    line = line.replace(r"\lfloor", "floor(")
    line = line.replace(r"\rfloor", ")")
    # Replace \left\lceil / \right\rceil
    line = re.sub(r"\\left\\lceil\s*(.*?)\s*\\right\\rceil", r"ceil(\1)", line)
    line = re.sub(r"\\lceil\s*(.*?)\s*\\rceil", r"ceil(\1)", line)
    line = line.replace(r"\lceil", "ceil(")
    line = line.replace(r"\rceil", ")")
    # Remove <video> tags
    line = re.sub(r"<video[^>]*>.*?</video>", "", line)
    line = re.sub(r"<video[^>]*/>", "", line)
    return line


def fix_content_for_typst(content):
    """Apply Typst-compatible math fixes to full file content."""
    # Remove only-html blocks (interactive applets, not suitable for PDF)
    content = strip_only_html_blocks(content)

    # Fix \left\lfloor ... \right\rfloor and \lfloor ... \rfloor
    # Use \s* to handle both spaced and non-spaced cases
    content = re.sub(
        r"\\left\\lfloor\s*(.*?)\s*\\right\\rfloor",
        r"floor(\1)",
        content,
    )
    content = re.sub(
        r"(?<!\\left)\\lfloor\s*(.*?)\s*\\rfloor(?!\\right)",
        r"floor(\1)",
        content,
    )

    # Replace \texttt{...} with quoted text (Typst doesn't have texttt)
    content = re.sub(r"\\texttt\{([^}]*)\}", r'"\1"', content)
    # Replace \textit{...} with just the content (Typst doesn't have textit)
    content = re.sub(r"\\textit\{([^}]*)\}", r"\1", content)
    # Replace \bmod with mod (Typst uses mod for binary modulo)
    content = content.replace(r"\bmod", "mod")

    # Remove <video> tags
    content = re.sub(r"<video[^>]*>.*?</video>", "", content)
    content = re.sub(r"<video[^>]*/>", "", content)

    # Add width: 100% to figure blocks without explicit width
    # (prevents oversized images in PDF)
    def add_figure_width(match):
        block = match.group(0)
        if "width:" not in block:
            block = block.replace("---\n", "---\nwidth: 100%\n", 1)
        return block

    content = re.sub(
        r"```\{figure\} .*?```",
        add_figure_width,
        content,
        flags=re.DOTALL,
    )

    # Inside {math} blocks, remove $ currency signs and replace \times
    # Pattern: match ```{math} ... ``` blocks
    def fix_math_block(match):
        block = match.group(0)
        # Remove $ before numbers and dots (currency like $2000, $1.000)
        block = re.sub(r"\$(\d)", r"\1", block)
        # Replace \times with times (Typst syntax)
        block = block.replace(r"\times", "times")
        return block

    content = re.sub(
        r"```\{math\}.*?```",
        fix_math_block,
        content,
        flags=re.DOTALL,
    )

    return content


def strip_only_html_blocks(content):
    """Remove <div class="only-html">...</div> blocks (interactive applets for PDF)."""
    result = []
    i = 0
    while i < len(content):
        pos = content.find('<div class="only-html">', i)
        if pos == -1:
            result.append(content[i:])
            break
        result.append(content[i:pos])
        i = pos + len('<div class="only-html">')
        depth = 1
        while i < len(content) and depth > 0:
            next_open = content.find("<div", i)
            next_close = content.find("</div>", i)
            if next_close == -1:
                i = len(content)
                break
            if next_open != -1 and next_open < next_close:
                depth += 1
                i = next_open + 4
            else:
                depth -= 1
                i = next_close + 6
    return "".join(result)


def process_file(filepath):
    """Applies regex transformations to a single markdown file using block buffering."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # First pass: fix content for Typst compatibility
    content = fix_content_for_typst(content)

    lines = content.splitlines(keepends=True)

    new_lines = []
    buffer = []
    in_block = False
    block_type = None
    block_header = ""
    block_fence = ""
    discard_block = False

    block_start_pattern = re.compile(r"^(\s*)(`{3,}|:{3,})\{([\w-]+)\}(.*)$")
    block_end_pattern = re.compile(r"^(\s*)(`{3,}|:{3,})\s*$")
    dark_mode_pattern = re.compile(r"class:.*only-dark-mode")

    for line in lines:
        if in_block:
            buffer.append(line)

            if dark_mode_pattern.search(line):
                discard_block = True

            match_end = block_end_pattern.match(line)
            if match_end:
                closing_fence = match_end.group(2)
                if closing_fence[0] == block_fence[0] and len(closing_fence) >= len(block_fence):
                    if discard_block:
                        pass
                    else:
                        if block_type == "admonition":
                            buffer[0] = buffer[0].replace("{admonition}", "{note}")
                            new_lines.extend(buffer)

                        elif block_type == "dropdown":
                            match = block_start_pattern.match(block_header)
                            if match:
                                title = match.group(4).strip()
                                indent = match.group(1)
                                new_lines.append(f"{indent}**{title}**\n\n")
                                if len(buffer) > 2:
                                    new_lines.extend(buffer[1:-1])
                            else:
                                new_lines.extend(buffer)

                        elif block_type == "tab-set":
                            tab_item_pattern = re.compile(r"^(\s*)(:{3,})\{tab-item\}\s*(.*)$")
                            tab_close_pattern = re.compile(r"^(\s*)(:{3,})\s*$")
                            for line in buffer[1:-1]:
                                m = tab_item_pattern.match(line)
                                if m:
                                    heading = m.group(3).strip()
                                    new_lines.append(f"{m.group(1)}**{heading}**\n\n")
                                elif tab_close_pattern.match(line):
                                    continue
                                else:
                                    new_lines.append(line)

                        elif block_type == "code-cell":
                            content_str = "".join(buffer)
                            if (
                                "show_dijkstra_step_by_step" in content_str
                                or "show_bellman_ford_step_by_step" in content_str
                            ):
                                new_lines.append(buffer[0])
                                indent = buffer[0][: len(buffer[0]) - len(buffer[0].lstrip())]
                                new_lines.append(f"{indent}---\n")
                                new_lines.append(f"{indent}tags: remove-output\n")
                                new_lines.append(f"{indent}---\n")
                                new_lines.extend(buffer[1:])
                            else:
                                new_lines.extend(buffer)

                        else:
                            new_lines.extend(buffer)

                    in_block = False
                    buffer = []
                    discard_block = False
                    block_type = None
                    block_header = ""
                    block_fence = ""

        else:
            match = block_start_pattern.match(line)
            if match:
                in_block = True
                block_fence = match.group(2)
                directive = match.group(3)
                block_header = line
                buffer.append(line)

                if directive == "admonition":
                    block_type = "admonition"
                elif directive == "dropdown":
                    block_type = "dropdown"
                elif directive == "tab-set":
                    block_type = "tab-set"
                elif directive == "code-cell":
                    block_type = "code-cell"
                else:
                    block_type = "other"
            else:
                new_lines.append(fix_line_for_typst(line))

    if buffer:
        new_lines.extend(buffer)

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


def clean_svg_files(directory):
    """Cleans SVG files for better Typst compatibility."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".svg"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                original = content
                # Remove draw.io content attribute (contains XML metadata with font refs)
                content = re.sub(r'\s+content="[^"]*"', "", content)
                # Remove duplicate XML attributes
                content = re.sub(r'(\s+\w+="[^"]*")\s*\1', r"\1", content)
                # Remove font-family attributes (Typst/resvg font subsetting compat)
                content = re.sub(r'\s*font-family="[^"]*"', "", content)
                if content != original:
                    print(f"  Cleaned {filepath}")
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content)


def process_directory(directory):
    """Recursively processes all .md files in the directory."""
    print(f"Processing markdown files in {directory}...")
    clean_svg_files(directory)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                process_file(os.path.join(root, file))


def build_typst():
    """Runs the myst build command to generate Typst + PDF."""
    cwd = TEMP_DIR
    cmd = ["myst", "build", "--execute", "--typst"]

    print(f"Running build command: {' '.join(cmd)} in {cwd}")
    try:
        subprocess.run(cmd, cwd=cwd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during build: {e}")
        sys.exit(1)


def post_process_typst():
    """Post-process generated typst files (fix arrows, headers)."""
    print("Post-processing Typst files...")
    build_temp_dir = os.path.join(TEMP_DIR, "_build", "temp")

    for root, dirs, files in os.walk(build_temp_dir):
        for file in files:
            if file.endswith(".typ"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                new_content = (
                    content.replace("arrow.r.double", "=>")
                    .replace("arrow.r", "->")
                    .replace("angle.l", "⟨")
                    .replace("angle.r", "⟩")
                    .replace("repeat-header: true", "repeat-header: false")
                    # Fix LaTeX math commands not converted by MyST
                    .replace("displaystyle ", "")
                    .replace("displaystyle", "")
                    .replace("quad", " ")
                    .replace(" land ", " ∧ ")
                    .replace("∧  ", "∧ ")
                )

                # Suppress "supplement: [Program]" in code figures (added by MyST)
                # Setting to "none" hides the supplement text while keeping Typst happy
                new_content = re.sub(
                    r"^(\s+)supplement: \[Program\],\s*$",
                    r"\1supplement: none,",
                    new_content,
                    flags=re.MULTILINE,
                )

                # Fix Typst raw text warnings: backtick fence followed by {
                # without space is interpreted as a language tag
                new_content = re.sub(
                    r"^(\s*`{3,})(\{\w[\w-]*\})",
                    r"\1 \2",
                    new_content,
                    flags=re.MULTILINE,
                )

                if content != new_content:
                    print(f"Fixed arrows in {file}")
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)

                # Return the path to the main typst file
                if "apunte-ayp2" in file:
                    main_typ_path = filepath

    return main_typ_path


def compile_pdf(typ_file):
    """Compiles the post-processed typst file to PDF."""
    print("Compiling final PDF...")
    cmd = ["typst", "compile", typ_file]
    print(f"Running: {' '.join(cmd)}")

    try:
        subprocess.run(cmd, cwd=os.path.dirname(typ_file), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during Typst compilation: {e}")
        sys.exit(1)

    return typ_file.replace(".typ", ".pdf")


def move_exports(generated_pdf):
    """Moves generated PDF to the exports directory."""
    dst_pdf = os.path.join(EXPORTS_DIR, "apunte-ayp2.pdf")

    if os.path.exists(generated_pdf):
        print(f"Moving {generated_pdf} to {dst_pdf}")
        os.makedirs(os.path.dirname(dst_pdf), exist_ok=True)
        shutil.copy2(generated_pdf, dst_pdf)
    else:
        print(f"Warning: Expected output file {generated_pdf} not found.")


def main():
    parser = argparse.ArgumentParser(description="Build PDF with pre-processing.")
    parser.add_argument("--chapter", help="Path to a specific chapter/file to build.")
    args = parser.parse_args()

    setup_temp_dir()
    process_directory(TEMP_DIR)

    # First run: generate .typ source (may fail compilation, that's OK)
    # Temporarily hide typst so myst only generates the .typ file
    env = os.environ.copy()
    orig_path = env.get("PATH", "")
    # Find and remove dirs containing typst from PATH
    new_path = ":".join(d for d in orig_path.split(":") if not os.path.exists(os.path.join(d, "typst")))
    env["PATH"] = new_path

    cwd = TEMP_DIR
    cmd = ["myst", "build", "--execute", "--typst"]
    print(f"Generating Typst source: {' '.join(cmd)}")
    subprocess.run(cmd, cwd=cwd, env=env, check=False)

    typ_file = post_process_typst()

    generated_pdf = compile_pdf(typ_file)

    if not args.chapter:
        move_exports(generated_pdf)


if __name__ == "__main__":
    main()
