import codecs

with codecs.open("..\data\hightemp.txt", "r", "utf_8_sig") as f:
    print("\n".join(set(i.split()[0] for i in f)))
