import codecs

f = codecs.open("..\data\hightemp.txt", "r", "utf_8_sig")
print("".join(i.replace("\t", " ") for i in f))
