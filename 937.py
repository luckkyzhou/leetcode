# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        strings = []
        nums = []
        for log in logs:
            if log[-1].isalpha():
                strings.append(log)
            else:
                nums.append(log)
        strings.sort(key=lambda x:(x[x.index(' ') + 1:], x[:x.index(' ') + 1]))
        return strings + nums