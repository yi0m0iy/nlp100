import sys
import codecs

if len(sys.argv) > 1:
    with codecs.open("..\data\hightemp.txt", "r", "utf_8_sig") as f:
        print("".join([i for i in f][-int(sys.argv[1]):]))
