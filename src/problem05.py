sentence = "I am an NLPer"
n = 2


def n_gram(n, itr):
    return [tuple(itr[i:i + n]) for i in range(len(itr) - n + 1)]

print(n_gram(n, sentence.split(" ")))
print(n_gram(n, sentence))
