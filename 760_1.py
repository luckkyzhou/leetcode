from typing import List
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        return list(map(B.index, A))