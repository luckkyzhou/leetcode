from collections import deque
from collections import defaultdict
import sys
from string import ascii_lowercase
import collections
from typing import List
import heapq
import math
import random
import itertools
import re

if __name__ == '__main__':
    a = "ccc"
    for match in re.finditer("cc", a):
        start = match.start()
        end = match.end()
        print("Found {} at {}:{}".format(a[start:end], start, end))