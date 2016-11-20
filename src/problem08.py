# from 04
sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. \
New Nations Might Also Sign Peace Security Clause. Arthur King Can."


def cipher(str):
    def convert_char(char):
        return chr(219 - ord(char)) if char.islower() else char

    return "".join(convert_char(i) for i in str)

print(cipher(sentence))
print(cipher(cipher(sentence)))
