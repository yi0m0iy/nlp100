from functools import reduce
from . import mediawiki
import re


class Parser(mediawiki.Parser):
    def filterLine(self, word: str):
        textlines = self.__text__.split("\n")
        return [line for line in textlines if word in line]

    def findall(self, pattern, *flags):
        def make_parser(match):
            if isinstance(match, tuple):
                return tuple(Parser(sub) for sub in match)
            else:
                return Parser(match)

        matches = self.__extract__(re.findall, pattern, *flags)
        return [make_parser(match) for match in matches]

    def search(self, pattern, group, *flags):
        match = self.__extract__(re.search, pattern, *flags)
        if not match:
            return Parser("")
        elif match.groups():
            return [Parser(sub) for sub in match.groups()]
        else:
            return Parser(match.group())

    def __bit_or__(self, a, b):
        return a | b

    def __extract__(self, func, pattern, *flags):
        bit_sum = reduce(self.__bit_or__, flags) if flags else 0
        return func(pattern, self.__text__, bit_sum)

    def sub(self, pattern, repl, *flags):
        bit_sum = reduce(self.__bit_or__, flags) if flags else 0
        result = re.sub(pattern, repl, self.__text__, flags=bit_sum)
        return Parser(result)
