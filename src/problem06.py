sentence1 = "paraparaparadise"
sentence2 = "paragraph"
n = 2
ex_bigram = "se"


def n_gram(n, itr):
    return set(itr[i:i + n] for i in range(len(itr) - n + 1))

set1 = n_gram(n, sentence1)
set2 = n_gram(n, sentence2)

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(ex_bigram in set1)
print(ex_bigram in set2)
