if __name__ == '__main__':
    num_list = [[0] * 2 for i in range(2)]
    print(num_list)
    dp = [[False for _ in range(3)] for _ in range(3)]
    print(dp)

    s = 'abcgefcba'
    l = 1
    r = 3
    res = s[l:r + 1]
    print(res)
