from collections import deque
import sys
from string import ascii_lowercase
import collections
from typing import List
import heapq


test = [(2, 0),(6, 1),(5, 1)]
test.sort(key=lambda x: (x[1], x[0]))
test1 = x[0] for x in test
print(test1)