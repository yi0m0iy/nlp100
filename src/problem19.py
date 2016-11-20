import codecs
from collections import Counter


with codecs.open("..\data\hightemp.txt", "r", "utf_8_sig") as f:
    col1 = [line.split()[0] for line in f]

counter = Counter(col1)
for word, cnt in counter.most_common():
    print(cnt, word)
