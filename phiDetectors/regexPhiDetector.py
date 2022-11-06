from pandas import DataFrame
import re

class RegexPhiDetector:

    def __init__(self) -> None:
        self._patterns = [
            re.compile("[A-Z][a-z]+")
        ]

    def detect(self, words: DataFrame) -> DataFrame:
        for pattern in self._patterns:
            words = words[ words.text.str.match(pattern) ]
        return words

