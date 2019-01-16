#!/usr/bin/env python
# -*-coding:utf-8-*-

def upper_attr(class_name, class_parents, class_attr):
    """
    返回一个对象,将属性都改为大写的形式
    :param class_name:  类的名称
    :param class_parents: 类的父类tuple
    :param class_attr: 类的参数
    :return: 返回类
    """
    # 生成了一个generator
    attrs = ((name, value) for name, value in class_attr.items() if not name.startswith('__'))
    uppercase_attrs = dict((name.upper(), value) for name, value in attrs)
    return type(class_name, class_parents, uppercase_attrs)

def run():
    __metaclass__ = upper_attr

    pw = upper_attr('Trick', (), {'bar': 0})
    print( hasattr(pw, 'bar'))
    print( hasattr(pw, 'BAR'))
    print( pw.BAR)

class UpperAttrMetaClass(type):
    def __new__(mcs, class_name, class_parents, class_attr):
        attrs = ((name, value) for name, value in class_attr.items() if not name.startswith('__'))
        uppercase_attrs = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaClass, mcs).__new__(mcs, class_name, class_parents, uppercase_attrs)


class TrickClass(object):
    __metaclass__ = UpperAttrMetaClass
    bar = 12
    money = 'unlimited'



def run_class_py2():
    print(TrickClass.__class__)
    print(TrickClass.__bases__)
    print(TrickClass.__metaclass__)
    print(TrickClass.__dict__)
    cla = TrickClass()
    print(cla.BAR)
    print(cla.MONEY)
    print(TrickClass.BAR)
    print(TrickClass.MONEY)


if __name__ == '__main__':

    run()
    run_class_py2()