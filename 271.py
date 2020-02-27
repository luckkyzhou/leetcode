class Codec:

    def encode (self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        if strs == []: return "null"
        return chr(257).join(strs)

    def decode (self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        if s == "null": return []
        return s.split(chr(257))