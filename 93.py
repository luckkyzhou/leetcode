class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seg_count = 4
        res = list()
        segments = [0] * seg_count

        def DFS(segIdx, segStart):
            if segIdx == seg_count:
                if segStart == len(s):
                    ip = ".".join(str(seg) for seg in segments)
                    res.append(ip)
                return

            if segStart == len(s):
                return

            if s[segStart] == '0':
                segments[segIdx] = 0
                DFS(segIdx+1, segStart+1)

            addr = 0
            for segEnd in range(segStart, len(s)):
                addr = addr*10 + (ord(s[segEnd]) - ord("0"))
                if 0 < addr <= 0xFF:
                    segments[segIdx] = addr
                    DFS(segIdx+1, segEnd+1)
                else:
                    break

        DFS(0, 0)
        return res