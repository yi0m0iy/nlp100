import re

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. \
New Nations Might Also Sign Peace Security Clause. Arthur King Can."
numbers = [1, 5, 6, 7, 8, 9, 15, 16, 19]
elements = dict()

pattern2 = r"[^,\.\s]+"

for count, word in enumerate(re.findall(pattern2, sentence)):
    if count + 1 in numbers:
        elements[word[0]] = count + 1
    else:
        elements[word[:2]] = count + 1

for k, v in sorted(elements.items(), key=lambda x: x[1]):
    print(k, v)
