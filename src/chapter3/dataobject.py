from .regexadapter import Parser
import json
import gzip


class Loader:
    def __init__(self, path, encoding="utf-8"):
        self.__path__ = path
        self.__encoding__ = encoding

    def get_data(self, title):
        with gzip.open(self.__path__, mode="rt",
                       encoding=self.__encoding__) as f:
            for line in f:
                data = json.loads(line)
                if data["title"] == title:
                    return Parser(data["text"])
        return None
