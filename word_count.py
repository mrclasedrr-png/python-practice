from collections import Counter
import re

try:
    with open('sample.txt', encoding="utf-8") as f:
        text = f.read()
    tl = text.lower()
    words = re.findall(r'\w+', tl)
    word_counts = Counter(words)
    for word, count in word_counts.most_common(10):
        print(f"{word:<11}{count:>6}")
except FileNotFoundError:
    print("File not found.")

