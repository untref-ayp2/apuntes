import re

filepath = "/home/martin/AyP2/apuntes/contenidos/_static/figures/funcion_acotada_dark.svg"
with open(filepath, "r") as f:
    content = f.read()

# I want to find the <text> elements containing n, 0, or = (1, 5) that have a dark fill
# We saw these have fill="rgb(68,68,68)" or similar in the previous find_label.py output
# Specifically, we saw:
# <text fill="rgb(68,68,68)" ...>0</text>
# <text fill="rgb(68,68,68)" ...> = (1, 5)</text>

# We also saw some text nodes with fill="#1e1e1e" in the extraction script earlier.


def replace_text_fill(match):
    tag_content = match.group(0)
    # If the text inside is one of our target labels
    if re.search(r">(?:n|0| = \(1, 5\))<", tag_content):
        # Replace the dark fill with white/light grey
        tag_content = tag_content.replace('fill="rgb(68,68,68)"', 'fill="#e0e0e0"')
        tag_content = tag_content.replace('fill="#1e1e1e"', 'fill="#e0e0e0"')
    return tag_content


# Match the whole <text ...>...</text> tag
content = re.sub(r"<text[^>]*>.*?</text>", replace_text_fill, content)

with open(filepath, "w") as f:
    f.write(content)
print("Surgical fix applied to n_0 label!")
