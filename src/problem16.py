# n(行ごとに)分割
import codecs
import sys
import itertools
import more_itertools


def genSuffix(n):
    alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
    for suf in itertools.product(alphabet, repeat=n):
        yield "".join(suf)

if len(sys.argv) > 1:
    with codecs.open("..\data\hightemp.txt", "r", "utf_8_sig") as f:
        text = f.readlines()

    suf = genSuffix(2)  # --suffix-length=2
    for sublist in more_itertools.chunked(text, int(sys.argv[1])):
        splitFile = "..\output\hightemp.split." + next(suf)
        with codecs.open(splitFile, "w", "utf8") as f:
            f.write("".join(sublist))
