#!/usr/bin/env python
# -*-coding:utf-8-*-
# Definition for a binary tree node.
from collections import Iterable


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        node = "val:{val} ".format(val=self.val)
        if self.left is not None:
            print(self.left.val)
            node += "left_val:{left_val}".format(left_val=self.left.val)
        if self.right is not None:
            print(self.right.val)
            node += "right_val:{right_val}".format(right_val=self.right.val)
        return node


class BinaryTree(object):

    def __init__(self, seq):
        assert (isinstance(seq, Iterable))
        self.root = None
        self.insert(*seq)

    def insert(self, *args):
        if not args:
            return
        if not self.root:
            self.root = TreeNode(args[0])
            args = args[1:]
        for i in args:
            seed = self.root
            while True:
                if i > seed.val:
                    if not seed.right:
                        node = TreeNode(i)
                        seed.right = node
                        break
                    else:
                        seed = seed.right
                else:
                    if not seed.left:
                        node = TreeNode(i)
                        seed.left = node
                        break
                    else:
                        seed = seed.left

    def minValue(self):
        node = self.root
        while node.left:
            node = node.left
        return node

    def maxValue(self):
        node = self.root
        while node.right:
            node = node.right
        return node

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left = root.left
        right = root.right
        left_deep = 1
        right_deep = 1
        while left is not None:
            if left is None:
                break
            left_deep += 1
            left = left.left

        while right is not None:
            if right is None:
                break
            right_deep += 1
            right = right.left
        deep = max(left_deep, right_deep)
        return deep


class HeadNode(object):
    def __init__(self, data, pnext=None):
        self.data = data
        self.pnext = pnext

    def __repr__(self):
        return self.data


class Head(object):

    def __init__(self):
        self.head = None
        self.__length = 0


    def isEmpty(self):
        return self.__length == 0

    def append(self, dataOrNode):
        if isinstance(dataOrNode, HeadNode):
            item = dataOrNode
        else:
            item = HeadNode(dataOrNode)
        if not self.head:
            self.head = item
            self.__length += 1
        else:
            node = self.head
            while node.pnext:
                node = node.pnext
            node.pnext = item
            self.__length += 1

    def delete_item(self, index):
        if self.isEmpty():
            print("error: out of index ")
            return
        if index == 0:
            self.head = self.head.pnext
            self.__length -= 1
            return
        j = 0
        node = self.head
        prev = self.head
        while node.pnext and j < index:
            prev = node
            node = node.pnext
            j += 1
        if j == index:
            prev.pnext = node
            self.__length -= 1

    def getItem(self,index):
        if index > self.__length or self.isEmpty() or index < 0:
            print("error: out of index ")
            return None
        i = 0
        node = self.head
        while node.pnext and i< index:
            node = node.pnext
        return node
    def getIndex(self,data):
        if self.isEmpty():
            print("error: is empty")
            return None
        j = 0
        node = self.head
        while node:
            if node.data ==data:
                return j
            node = node.pnext
            j += 1
        return node


    def insert(self, node):
        pass


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left = root.left
        right = root.right
        left_deep = 1
        right_deep = 1
        while left is not None:
            if left is None:
                break
            left_deep += 1
            left = left.left

        while right is not None:
            if right is None:
                break
            right_deep += 1
            right = right.left
        deep = max(left_deep, right_deep)
        return deep


if __name__ == '__main__':
    # args = [1, 2, 5, 6, 11, 9, 0]
    # B_tree = BinaryTree(args)
    # print(B_tree.root.val)
    # max_value = B_tree.maxValue()
    # min_value = B_tree.minValue()
    # print(max_value, min_value)
    head_obj = Head()
    data = [1,2,4,5,8,9,4,3]
    for i in data:
        head_obj.insert(i)
