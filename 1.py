# -*- coding:utf-8 -*-

nums = [2,7,11,15]
target = 9


def twoSum(nums, target):

    hashmap = {}
    for index, num in enumerate(nums):
        another_num = target - num
        if another_num in hashmap:
            return hashmap[another_num], index
        hashmap[num] = index
    return None

if __name__ == '__main__':
    print twoSum(nums,target)