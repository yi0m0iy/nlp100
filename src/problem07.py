x = 12
y = "気温"
z = 22.4


def gen_sentence(x, y, z):
    return "{0}時の{1}は{2}".format(x, y, z)

print(gen_sentence(x, y, z))
