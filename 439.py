class Solution:
    def parseTernary(self, expression: str) -> str:
        expression = list(expression)
        cur = []

        while expression:
            x = expression.pop()
            if x == '?':
                if expression.pop() == 'T':
                    y = cur.pop()
                    cur.pop()
                    cur.append(y)
                else:
                    cur.pop()
            elif x != ':':
                cur.append(x)
        return cur[0]