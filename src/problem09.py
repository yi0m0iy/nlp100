import random

sentence = "I couldn't believe that I could actually understand \
what I was reading : the phenomenal power of the human mind ."


def typoglycemia(str):
    def shaffle(word):
        if len(word) > 4:
            substring = "".join(random.sample(word[1:-1], len(word) - 2))
            return word[0] + substring + word[-1]
        else:
            return word

    return " ".join(shaffle(i) for i in str.split())

print(typoglycemia(sentence))
