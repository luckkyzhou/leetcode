
def maxSubstring(s):
    # Write your code here
    win, ret, res = [], [], []
    for k in range(len(s)):
        for i, v in enumerate(s):
            if i >= k and win and win[0] <= i - k: win.pop(0)
            while win and s[win[-1]] <= v: win.pop()
            win.append(i)
            if i >= k - 1: ret.append(s[win[0]])
    return ret

if __name__ == '__main__':
    res = maxSubstring('ba')
    print(res)