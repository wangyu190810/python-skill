#!/usr/bin/env python
# -*-coding:utf-8-*-

import random
def get_randint_list(length):
    data_list = []
    for _ in range(length):
        data = random.randint(1,100)
        data_list.append(data)
    # data = []
    return data_list

def sort_data(data,mod):
    length = len(data)
    sort_list = []
    for row in range(0,length,mod):
        _stmt_ = []
        if (row + mod) >= length:
            end = length
        else:
            end = row + mod
        sort_list.append(data[row:end])
    return sort_list

def tuple_min_arge(data,mod=2):
    # for row in range(mod):
    if data[0] > data[1]:
        data[0],data[1] = data[1],data[0]
    return data

def five_min_arge(data,mod=4):
    if data[0][1] >= data[1][0]:
        return data
    elif data[0][0] <= data[1][1]:
        data = data[1][0],data[1][1],data[0][0],data[0][1]
    elif data[0][1] <= data[1][0]:
        data = data[0],data[1] = data[1], data[0]
    elif data[0][0] <= data[1][0] and data[0][1] <= data[1][1]:
        data = data[0][0],data[1][0],data[0][1],data[1][1]
    elif data[0][0] <= data[1][0] and data[0][1] >= data[1][1]:
        data = data[0][0],data[1][0],data[1][1],data[0][1]
    elif data[0][0] >= data[1][0] and data[0][1] <= data[1][1]:
        data = data[1][0], data[0][0], data[0][1], data[1][1]
    elif data[0][0] >= data[1][0] and data[0][1] >= data[1][1]:
        data = data[0][0], data[1][0], data[0][1], data[1][1]
    return data

if __name__ == '__main__':
    will_sort_data = get_randint_list(11)
    sort_list = sort_data(will_sort_data,2)
    print(will_sort_data)
    print(sort_list)
    five_data = []
    tuple_data_0 = tuple_min_arge(sort_list[0])
    five_data.append(tuple_data_0)
    tuple_data_1 = tuple_min_arge(sort_list[1])
    five_data.append(tuple_data_1)
    print(tuple_data_0)
    print(tuple_data_1)
    print(five_min_arge(five_data))
    #
    # for row in  range(0,len(tuple_min_arge(sort_list[1])),2):
    #     print(five_min_arge(row))
    # tuple_sort =

    # print(tuple_sort)