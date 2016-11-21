import re
from abc import ABCMeta, abstractmethod


class Parser(metaclass=ABCMeta):
    MULTILINE = re.MULTILINE
    DOTALL    = re.DOTALL

    def __init__(self, text: str):
        self.__text__ = text

    def __repr__(self):
        return self.__text__

    def __len__(self):
        return len(self.__text__)

    def filterCategoryLine(self):
        return self.filterLine("Category")

    def filterCategory(self):
        pattern = r"Category:([^\|\]]+)"
        return self.findall(pattern)

    def filterSection(self):
        pattern = r"([^=\s]+)\s?=(=+)$"
        matches = self.findall(pattern, self.MULTILINE)
        return {section: len(level) for section, level in matches}

    def filterFileName(self):
        pattern = r"(?:File|ファイル):([^\|]+)"
        return self.findall(pattern)

    def filterBasicInfo(self):
        pattern = r"\{\{基礎情報.*?\n\|(.*?\n)\}\}"
        return self.search(pattern, self.MULTILINE, self.DOTALL)[0]

    def templateToDict(self):
        pattern = r"(.*?)\s=\s(.*?)\n[\|\Z]"
        matches = self.findall(pattern, self.MULTILINE, self.DOTALL)
        return {str(k): v for k, v in matches}

    def delAccent(self):
        pattern = r"'{2,5}"
        repl = r""
        return self.sub(pattern, repl)

    def delInnerLink(self):
        pattern = (
            r"\[{2}(?!File|ファイル)"  # 否定先読み
            r".*?([^\|]+?)\]{2}"
        )
        repl = r"\1"
        return self.sub(pattern, repl)

    def delFile(self):
        pattern = r"\[{2}(?:File|ファイル):([^\|]+).*?\]{2}"
        repl = r"\1"
        return self.sub(pattern, repl)

    def delReference(self):
        pattern = r"<ref[^<]*?(/>|>.*?</ref>)"
        repl = r""
        return self.sub(pattern, repl, self.DOTALL)

    def replacePond(self):
        pattern = r"&pound;"
        repl = "£"
        return self.sub(pattern, repl)

    def delLang(self):
        pattern = r"\{{2}lang\|.*?\|(.*?)\}{2}"
        repl = r"\1"
        return self.sub(pattern, repl)

    def delBR(self):
        pattern = r"<br\s?/>"
        repl = r""
        return self.sub(pattern, repl)

    @abstractmethod
    def filterLine(self, word: str):
        return list()

    @abstractmethod
    def findall(self, pattern, *flags):
        return list()

    @abstractmethod
    def search(self, pattern, group, *flags):
        return object()

    @abstractmethod
    def sub(self, pattern, repl, *flags):
        return object()
