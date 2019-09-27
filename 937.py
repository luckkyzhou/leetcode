# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        strList = []
        numList = []
        for log in logs:
            if log[-1].isalpha():
                strList.append(log)
            else:
                numList.append(log)
        strList.sort(key=lambda x:(x[x.index(' ') + 1]))
        return strList + numList