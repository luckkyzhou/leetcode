def getMinimumDifference(a, b):
    # Write your code here
    res = []
    for i in range(len(a)):
        if len(a[i]) != len(b[i]):
            res.append(-1)
            continue
        aList = list(a[i])
        bList = list(b[i])
        count = 0

        while aList:
            if aList[0] not in bList:
                count += 1
                aList.pop(0)
            else:
                bList.pop(bList.index(aList[0]))
                aList.pop(0)
        res.append(count)
    return res