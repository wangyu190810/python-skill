#!/usr/bin/env python
# -*-coding:utf-8-*-
import random
import unittest

def get_randint_list(nums=10):
    data_list = []
    for _ in range(nums):
        data = random.randint(1, 100)
        data_list.append(data)
    # data = []
    return data_list

def sort_data(sort_list):
    compare_num = sort_list[0]
    head_list = []
    tail_list = []
    end_list = []
    for row in sort_list[1:]:
        if row > compare_num:
            tail_list.append(row)
        else:
            head_list.append(row)
    end_list.append(head_list)
    end_list.append([compare_num])
    end_list.append(tail_list)
    return end_list

#quick sort
def quickSort(array):
    if len(array) < 2:  # 基线条件（停止递归的条件）
        return array
    else:  # 递归条件
        baseValue = array[0]  # 选择基准值
        # 由所有小于基准值的元素组成的子数组
        less = [m for m in array[1:] if m < baseValue]
        # 包括基准在内的同时和基准相等的元素，在上一个版本的百科当中，并没有考虑相等元素
        equal = [w for w in array if w == baseValue]
        # 由所有大于基准值的元素组成的子数组
        greater = [n for n in array[1:] if n > baseValue]
        print(less,equal,greater)
    return quickSort(less) + equal + quickSort(greater)

if __name__ == '__main__':
    randint_list = get_randint_list(7)
    print(randint_list)
    fast_end_list = []
    end_list = quickSort(randint_list)
    # end_list = sort_data(randint_list)
    # flag = 1
    # # while flag:
    # for index,row in enumerate(end_list):
    #     if len(row) > 2:
    #         fast_end_list = sort_data(row)
    #         flag = 0
    #
    # # print(randint_list)
    print(end_list)
    print(fast_end_list)