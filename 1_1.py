# -*- coding:utf-8 -*-

def twoSum(nums,target):
    hashmap = {}
    for index,num in enumerate(nums):
        hashmap[num] = index

    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and j != i:
            return [i,j]

if __name__ == '__main__':
    print(twoSum([2,7,11],9))
