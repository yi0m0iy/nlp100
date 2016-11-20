import gzip
import json
import re
import codecs
from functools import reduce
from urllib.parse import urlencode
from urllib.request import urlopen


class Chapter3:
    def __init__(self,
                 path="..\data\jawiki-country.json.gz",
                 title="イギリス",
                 encoding="utf-8"):
        self.path = path
        self.title = title
        self.encoding = encoding
        self.__load_obj()

    def __load_obj(self):
        with gzip.open(self.path, mode="rt", encoding="utf-8") as f:
            data = {"title": "", "text": ""}
            while data["title"] != self.title:
                line = f.readline()
                if line:
                    data = json.loads(line)
                else:
                    self.data = None
                    return
            else:
                self.data = data

    def __run_filter(self, func, pattern, text, *flags):
        def bit_or(a, b):
            return a | b

        bit_sum = reduce(bit_or, flags) if flags else 0
        return func(pattern, text, bit_sum)

    def findall(self, pattern, *flags):
        return self.__run_filter(re.findall, pattern,
                                 self.data["text"], *flags)

    def findall_text(self, pattern, text, *flags):
        return self.__run_filter(re.findall, pattern, text, *flags)

    def search(self, pattern, *flags):
        return self.__run_filter(re.search, pattern,
                                 self.data["text"], *flags)

    def get_template(self):
        templ_pttrn = r"\{\{基礎情報.*?^\|(.*?)^\}\}"
        templ = self.search(templ_pttrn, re.MULTILINE, re.DOTALL)
        if templ:
            elements = templ.group(1)
            element_pttrn = r"(.*?)\s=\s(.*?)(?:^\||\Z)"
            key_value = self.findall_text(element_pttrn, elements,
                                          re.MULTILINE, re.DOTALL)
            return {t[0]: t[1] for t in key_value if t}
        else:
            return dict()

    def problem20(self):
        return self.data["text"]

    def problem21(self):
        textlines = self.data["text"].split("\n")
        return [line for line in textlines if "Category" in line]

    def problem22(self):
        # [[Category:THISISCATEGORYNAME]]
        # [[Category:THISISCATEGORYNAME|sortkey]]
        pattern = r"Category:([^\|\]]+)"
        return self.findall(pattern)

    def problem23(self):
        # ===THISISSECTIONNAME{= * (sectionlevel + 1)
        pattern = r"([^=\s]+)\s?=(=+)$"
        matches = self.findall(pattern, re.MULTILINE)
        return [(match[0], len(match[1]))
                for match in matches if match]

    def problem24(self):
        # File:THISISFILENAME|etc
        # ファイル:THISISFILENAME|etc
        pattern = r"(?:File|ファイル):([^\|]+)"
        return self.findall(pattern)

    def problem25(self):
        return self.get_template()

    def problem26(self):
        basic_info = self.get_template()
        pttrn = r"'{2,5}"
        return {k: re.sub(pttrn, r"", v) for k, v in basic_info.items()}

    def problem27(self):
        def del_markup(text):
            pttrn_highlight = r"'{2,5}"
            repl_highlight = r""
            pttrn_innrlink = r"\[{2}(?!File|ファイル).*?([^\|]+?)\]{2}"
            repl_innrlink = r"\1"
            intertext = re.sub(pttrn_highlight, repl_highlight, text)
            return re.sub(pttrn_innrlink, repl_innrlink, intertext)
        basic_info = self.get_template()
        return {k: del_markup(v) for k, v in basic_info.items()}

    def problem29(self):
        def del_markup(text):
            pttrn_file = r"\[{2}(ファイル|File):(.*?)\|.*?\]{2}"
            repl_file = r"\2"
            return re.sub(pttrn_file, repl_file, text)
        basic_info = self.get_template()
        file_info = {k: del_markup(v)
                     for k, v in basic_info.items()}["国旗画像"]

        prefix = "https://ja.wikipedia.org/w/api.php?"
        query = {
            "format": "json",
            "action": "query",
            "titles": "File:{0}".format(file_info),
            "prop": "imageinfo",
            "iiprop": "url"
        }
        uri = prefix + urlencode(query)
        reader = codecs.getreader("utf8")
        with urlopen(uri) as resp:
            file_obj = json.load(reader(resp))

        return file_obj["query"]["pages"]["-1"]["imageinfo"][0]["url"]


if __name__ == "__main__":
    chap = Chapter3()
    # print(chap.problem20())
    # print(*chap.problem21(), sep="\n")
    # print(*chap.problem22(), sep="\n")
    # for name_level in chap.problem23():
    #     print(*name_level)
    # print(*chap.problem24(), sep="\n")
    # for item in chap.problem25().items():
    #     print(*item, end="")
    # for item in chap.problem25().items():
    #     print(*item, end="")
    # for item in chap.problem26().items():
    #     print(*item, end="")
    # for item in chap.problem27().items():
    #     print(*item, end="")
    print(chap.problem29())
