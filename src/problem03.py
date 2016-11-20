import math
import re

sentence = "Now I need a drink, alcoholic of course, \
after the heavy lectures involving quantum mechanics."

print(math.pi)

print([len(i.rstrip(",").rstrip(".")) for i in sentence.split(" ")])

pattern = r"[,\.\s]+"
print([len(i) for i in re.split(pattern, sentence)][:-1])

pattern2 = r"[^,\.\s]+"
print([len(i) for i in re.findall(pattern2, sentence)])
