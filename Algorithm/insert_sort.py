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
    end_list = [compare_num]
    head_list = []
    tail_list = []
    for row in sort_list[1:]:
        if row > compare_num:
            tail_list = compare_nums(tail_list, row)
        else:
            head_list = compare_nums(head_list, row)
    print(head_list, tail_list)
    return head_list + end_list + tail_list


def compare_nums(head_list, nums):
    head_list.append(nums)
    head_list_len = len(head_list)
    if head_list_len == 1:
        return head_list
    for head_index, _ in enumerate(head_list):
        if head_list_len - head_index - 1 > 0:
            # head_index = head_index + 1
            # print(head_list_len - head_index)
            if head_list[head_list_len - head_index - 1] < head_list[head_list_len - head_index - 2]:

                head_list[head_list_len - head_index - 1], \
                head_list[head_list_len - head_index - 2] = head_list[
                                                                head_list_len - head_index - 2], \
                                                            head_list[
                                                                head_list_len - head_index - 1]

    return head_list

class TestStringMethods(unittest.TestCase):

    def test_insert_sort(self):
        randint_list = get_randint_list()
        insert_sort_data = sort_data(randint_list)
        randint_list.sort()
        self.assertListEqual(randint_list,insert_sort_data)


if __name__ == '__main__':
    randint_list = get_randint_list()
    print(randint_list)
    end_list = sort_data(randint_list)
    # print(randint_list)
    print(end_list)
    unittest.main()
