import re

filepath = "/home/martin/AyP2/apuntes/contenidos/_static/figures/funcion_acotada_dark.svg"
with open(filepath, "r") as f:
    content = f.read()

# Look for the dark color I found earlier: #1e1e1e and rgb(68,68,68)
results = re.finditer(r'(fill="(?:#1e1e1e|rgb\(68,68,68\))")', content)

for match in results:
    start = max(0, match.start() - 200)
    end = min(len(content), match.end() + 200)
    print(f"--- Found at {match.start()} ---\n{content[start:end]}\n")
