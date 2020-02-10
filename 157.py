def read4(buf) -> int:
    pass

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        cur = 0
        while n > 0:
            cache = [" "] * 4
            r = read4(cache)
            tmp = min(r, n)
            buf[cur : cur+tmp] = cache
            cur += tmp
            if tmp < 4: break
            n -= 4
        return cur