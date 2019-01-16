#!/usr/bin/env python
# -*-coding:utf-8-*-



class UpperAttrMetaClass(type):
    def __new__(mcs, class_name, class_parents, class_attr):
        attrs = ((name, value) for name, value in class_attr.items() if not name.startswith('__'))
        uppercase_attrs = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaClass, mcs).__new__(mcs, class_name, class_parents, uppercase_attrs)

class TrickClassPy3(metaclass=UpperAttrMetaClass):
    bar = 12
    money = 'unlimited'

def run_class_py3():

    print(TrickClassPy3.__class__)
    print(TrickClassPy3.__bases__)
    # print(TrickClassPy3.__metaclass__)
    print(TrickClassPy3.__dict__)
    cla = TrickClassPy3()
    print(cla.BAR)
    print(cla.MONEY)
    print(TrickClassPy3.BAR)
    print(TrickClassPy3.MONEY)




if __name__ == '__main__':

    # run()
    # run_class_py2()
    run_class_py3()
