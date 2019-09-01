# -*- coding:utf-8 -*-

def twoSum(nums,target):
    hashmap = {}
    result_list = []
    for index,num in enumerate(nums):
        hashmap[num] = index
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and j != i:
            result_list.append((i,j))
            continue
        return result_list

if __name__ == '__main__':

    print(twoSum([2,7,3,6,11],9))