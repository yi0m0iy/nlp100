from os.path import join as join_path
from .dataobject import Loader
import requests

json_path = join_path(__file__, "..\..\..\data\jawiki-country.json.gz")
title = "イギリス"
url = "https://ja.wikipedia.org/w/api.php"


def print_problem(n: int):
    output_partition = "+++++Problem{:d}+++++"
    print(output_partition.format(n))


parser = Loader(json_path).get_data(title)

print_problem(20)
print(parser)

print_problem(21)
print(*parser.filterCategoryLine(), sep="\n")

print_problem(22)
print(*parser.filterCategory(), sep="\n")

print_problem(23)
for name, level in parser.filterSection().items():
    print(name, level)

print_problem(24)
print(*parser.filterFileName(), sep="\n")

basic_info = parser.filterBasicInfo()

print_problem(25)
for k, v in basic_info.templateToDict().items():
    print(k, v, sep=" = ")

no_accent = basic_info.delAccent()

print_problem(26)
for k, v in no_accent.templateToDict().items():
    print(k, v, sep=" = ")

no_innerlink = no_accent.delInnerLink()

print_problem(27)
for k, v in no_innerlink.templateToDict().items():
    print(k, v, sep=" = ")

plain_info = (no_innerlink.delFile()
              .delReference()
              .replacePond()
              .delLang()
              .delBR()
              .templateToDict())

print_problem(28)
for k, v in plain_info.items():
    print(k, v, sep=" = ")

print_problem(29)
query = {
    "format": "json",
    "action": "query",
    "titles": "File:{}".format(plain_info["国旗画像"]),
    "prop": "imageinfo",
    "iiprop": "url"
}
response = requests.get(url, params=query).json()
print(response["query"]["pages"]["-1"]["imageinfo"][0]["url"])
