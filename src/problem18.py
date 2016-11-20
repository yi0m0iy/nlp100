import codecs


def colgetter(n):
    def getcol(line):
        return line.split()[n]
    return getcol

with codecs.open("..\data\hightemp.txt", "r", "utf_8_sig") as f:
    for line in sorted(f.readlines(), key=colgetter(2), reverse=True):
        print(line, end="")
