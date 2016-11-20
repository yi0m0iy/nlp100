word = "パタトクカシーー"
print(word[1::2])
print("".join([y for x, y in enumerate(word) if x % 2 == 1]))
