#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
选择排序
"""
import random
def get_randint_list():
    data_list = []
    for _ in range(100):
        data = random.randint(1,100)
        data_list.append(data)
    # data = []
    return data_list

def sort_data(data):
    min_age = 0
    min_index = -1
    for index,val in enumerate(data):
        if index ==0:
            min_age = val
            min_index = index
        elif val < min_age:
            min_age = val
            min_index = index
    print(min_age,min_index)
    if min_index > -1:
        del data[min_index]
    return min_age,data

def for_sort_list(data):
    select_list = []
    len_data = data
    for _ in  range(len(len_data)):

        min_age, surplus_data = sort_data(data=data)
        select_list.append(min_age)
        data = surplus_data
    return select_list

if __name__ == '__main__':
    data = get_randint_list()
    print(data)
    # min_age,surplus_data = sort_data(data=data)
    # print(min_age,surplus_data)
    select_data_end = for_sort_list(data)
    print(select_data_end)