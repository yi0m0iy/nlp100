def joinTab(*words):
    return "\t".join(*words)


def delReturn(word):
    return word.rstrip("\n").rstrip("\r")


def merge(*Cols):
    return [joinTab(delReturn(i) for i in k) for k in zip(*Cols)]

if __name__ == "__main__":
    import codecs

    with codecs.open("..\output\col1.txt", "r", "utf-8") as f:
        col1 = f.readlines()

    with codecs.open("..\output\col2.txt", "r", "utf-8") as f:
        col2 = f.readlines()

    with codecs.open("..\output\merge.txt", "w", "utf-8") as f:
        f.write("\n".join(merge(col1, col2)))
