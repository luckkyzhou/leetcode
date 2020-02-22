class ZigzagIterator(object):

    def __init__ (self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.zigzag = []
        i = 0
        if v1 and v2:
            while i < min(len(v1), len(v2)):
                self.zigzag.append(v1[i])
                self.zigzag.append(v2[i])
                i += 1
        if v1[i:]: self.zigzag += v1[i:]
        elif v2[i:]: self.zigzag += v2[i:]


    def next (self):
        """
        :rtype: int
        """
        if self.zigzag: return self.zigzag.pop(0)

    def hasNext (self):
        """
        :rtype: bool
        """
        return self.zigzag != []