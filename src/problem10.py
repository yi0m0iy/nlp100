import codecs

print(len([None for line in codecs.open("..\data\hightemp.txt", "r", "utf_8_sig")]))
