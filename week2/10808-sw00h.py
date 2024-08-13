from collections import Counter
import string

text = input()
counter = Counter(text)

alphabet_count = dict.fromkeys(string.ascii_lowercase, 0)

for letter, count in counter.items():
    if letter in alphabet_count:
        alphabet_count[letter] += count

print(*alphabet_count.values())