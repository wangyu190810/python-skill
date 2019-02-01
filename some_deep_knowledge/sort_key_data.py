#!/usr/bin/env python
# -*-coding:utf-8-*-
import random

# a = random.randint(10,50)

def get_data_list():
    data = []
    for row in range(10):
        _stmt_ = random.randint(10, 50)
        data.append(str(_stmt_))
    return data
data = get_data_list()
data1 = get_data_list()
data2 = data1.copy()
data2.sort()
# print(data)
# print(data1)
# print(data2)
# data3 = data2[:5]
# print(data3)

sort_data = ['15', '16', '25', '29', '30', '38', '40', '47', '49', '50']
end_str = ['38', '30', '40', '15', '16', '49']
def all_sort_data(sort_data,end_str):
    select_data_end = []
    for value in sort_data:
        if value in end_str:
            select_data_end.append(value)
    return select_data_end
    # print(select_data_end)

def forzen_sort_data(sort_data,end_str):
    end_str = frozenset(end_str)
    intersection = [x for x in sort_data if x in end_str]
    return intersection

if __name__ == '__main__':
    all_sort_data(sort_data=sort_data,end_str=end_str)
    forzen_sort_data(sort_data=sort_data, end_str=end_str)