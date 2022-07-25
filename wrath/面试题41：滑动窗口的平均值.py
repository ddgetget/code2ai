#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-07-15 05:40
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    面试题41：滑动窗口的平均值.py
# @Project: code2ai
# @Package: 
# @Ref:
"""
题目：请实现如下类型MovingAverage，计算滑动窗口中所有数字的平均值，该类型构造函数的参数确定滑动窗口的大小，
每次调用成员函数next时都会在滑动窗口中添加一个整数，并返回滑动窗口中所有数字的平均值。
"""
from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        # 限制队列的长度
        self.size = size
        # 类似于list的容器，可以快速的在队列头部和尾部添加、删除元素
        self.queue = deque()
        # 用于计数已经存取的个数
        self.sum = 0

    def next(self, val: int) -> float:
        # 对添加的数据进行添加
        self.sum += val
        # 在队列的尾部添加一个数据
        self.queue.append(val)
        # 判断队列的长度与限定的长度
        if len(self.queue) > self.size:
            # 真毒队列长度超过限定长度，从左边去除一个
            self.sum -= self.queue.popleft()
        # 计算新的队列的均值
        return self.sum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

if __name__ == '__main__':
    print(MovingAverage(2).next(8))
