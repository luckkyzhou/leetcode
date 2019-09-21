from collections import deque
if __name__ == '__main__':
    '''
    num_list = [[0] * 2 for i in range(2)]
    print(num_list)
    dp = [[False for _ in range(3)] for _ in range(3)]
    print(dp)

    s = 'abcgefcba'
    l = 1
    r = 3
    res = s[l:r + 1]
    print(res)
    
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    m = len(grid)
    n = len(grid[0])
    queue = deque()
    #queue.append((1,1,1))
    if queue:
        x, y, z = queue.popleft()
        print(x,y)
        print(queue)
    else:
        print(m)
    

    n = [1, 2, 3, 4, 5]
    #print(n[-1])

    m = [0 for x in range(4)]
    for i in range(1, 4):
        print(m[i])
    '''
    res = 'Twenty '
    while res[-1] == ' ':
        res = res[:-1]
    print(res)