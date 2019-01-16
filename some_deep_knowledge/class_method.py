#!/usr/bin/env python
# -*-coding:utf-8-*-
import unittest
import pprint

class Reverse(object):
    """实现对类迭代"""
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


class ClassDir(object):
    """类内部函数探究"""

    STATUS_STRING = "status_string"

    def __new__(cls, *args, **kwargs):
        """使用new作为单例函数，函数实例化从new开始，而不是从__init__开始"""
        if not hasattr(cls,"_object"):
            cls._object = object.__new__(cls)
        return cls._object

    def __init__(self,name):
        self.name = name

    def __eq__(self, other):
        if self.STATUS_STRING == other.STATUS_STRING:
            return True
        else:
            return False

    def __format__(self, format_spec):
        if isinstance(self.name,str):
            return  format_spec + self.name.upper() + format_spec
        return self.name

    def __str__(self):
        """打印输出数据，根据要求定制化打印"""
        if isinstance(self.name, str):
            return self.name.upper()
        else:
            return self.name







class Unittest(unittest.TestCase):

    def setUp(self):
        self.class_dir_who = ClassDir("who")
        self.class_dir_hello = ClassDir("who")

    def test_Reverse_class(self):
        self.reverse_data = [1,2,54,6]
        self.obj_Reverse = Reverse(self.reverse_data)
        length = len(self.reverse_data)
        nums = 0
        for row in self.reverse_data:
            nums += 1
        else:
            self.assertEqual(length,nums)

    def test_class_dir_eq(self):
        self.assertEqual(self.class_dir_hello,self.class_dir_who)




if __name__ == '__main__':
    unittest.main()
