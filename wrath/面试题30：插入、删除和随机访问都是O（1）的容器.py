#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-07-16 20:13
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    面试题30：插入、删除和随机访问都是O（1）的容器.py
# @Project: code2ai
# @Package: 
# @Ref:

"""
题目：设计一个数据结构，使如下3个操作的时间复杂度都是O（1）。
·insert（value）：如果数据集中不包含一个数值，则把它添加到数据集中。
·remove（value）：如果数据集中包含一个数值，则把它删除。
·getRandom()：随机返回数据集中的一个数值，要求数据集中每个数字被返回的概率都相同
"""
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 用来存储添加的排名，也就是说头一次添加的名次
        self.hash = {}
        # 赢一个列表来存取所有的数据，这里根据下面的情况，可以当成set类型，设置的阈值其实是数据的个数，所有永远不会有冲突
        self.stack = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        # 针对插入的值已经存在hash表中
        if val in self.hash:
            # 不需要再次插入了
            return False
        # 在确保之前没有添加过的情况，用一个列表存储，新添加的数据
        self.stack.append(val)
        # 并数一下之前的数据个数，好给新的数据天剑一个下标位置
        self.hash[val] = len(self.stack) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # 真滴不在表中的，只能返回False
        if val not in self.hash: return False
        # 如果在表中，减少一个数据，表的阈值可以变小
        last = len(self.stack) - 1
        # 获取需要删除值的索引
        tar = self.hash[val]
        # 获取表最后一个的索引
        tar_num = self.stack[-1]
        
        self.stack[last], self.stack[tar] = self.stack[tar], self.stack[last]
        self.stack.pop()
        self.hash[tar_num] = tar
        del self.hash[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.stack)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
