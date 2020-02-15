from typing import List
from itertools import zip_longest
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        col = ["".join(w) for w in zip_longest(*[word for word in words], fillvalue="")]
        return col == words