
def countPairs(arr, k):
    res = []
    hashmap = {}

    for ar in arr:
        if k - ar in arr and k - ar != ar:
            if (ar, k - ar) not in res and  (k - ar, ar) not in res:
                res.append((ar, k - ar))
    for key in arr:
        hashmap[key] = hashmap.get(key, 0) + 1
    for key in hashmap.keys():
        if hashmap[key] >= 2 and 2 * key == k:
            res.append((key, key))
    return res

if __name__ == '__main__':
    res = countPairs([6,6],12)
    print(res)
