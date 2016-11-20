import codecs

with codecs.open("..\data\hightemp.txt", "r", "utf_8_sig") as f:
    text = f.readlines()

with codecs.open("..\output\col1.txt", "w", "utf-8") as f:
    f.write("\n".join(i.split()[0] for i in text))

with codecs.open("..\output\col2.txt", "w", "utf-8") as f:
    f.write("\n".join(i.split()[1] for i in text))
