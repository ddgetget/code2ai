#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-07-11 17:24
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    面试题59：数据流的第k大数字.py
# @Project: wrath
# @Package: 
# @Ref:
"""
题目：请设计一个类型KthLargest，它每次从一个数据流中读取一个数字，并得出数据流已经读取的数字中第k
（k≥1）大的数字。该类型的构造函数有两个参数：一个是整数k
，另一个是包含数据流中最开始数字的整数数组nums（假设数组nums的长度大于k
）。该类型还有一个函数add，用来添加数据流中的新数字并返回数据流中已经读取的数字的第k
大数字。
"""
import heapq
from typing import List


class KthLargest:

    """"
    第K大，肯定是需要升序排列，然后从前往后数第K个
    """

    def __init__(self, k: int, nums: List[int]):
        # 弄一个小根堆，用列表存储
        self.HEAP = []
        self.size = k

        for num in nums:
            self._push(num)

    def _push(self, num):
        # 真滴存储的列表长度小于K的情况，说明还需要继续往大根堆里面添加，
        if len(self.HEAP) < self.size:
            # heapq是Python默认的堆，默认是小顶堆，即小根堆，往HEAP里面添加
            heapq.heappush(self.HEAP, num)
            """
            def heappush(heap, item):
                heap.append(item)
                _siftdown(heap, 0, len(heap)-1)
            """
        else:
            # 针对列表存储已经满了，列表第一个看是不是小于第k+1个元素
            if self.HEAP[0] < num:
                # 因为是找前K大，所以遇到小值，需要把最后一个删了，重新替换成较大的一个
                heapq.heappop(self.HEAP)
                # 替换成较大的一个，后续这个列表是固定长度的
                heapq.heappush(self.HEAP, num)

    def add(self, val: int) -> int:
        # 这一步跟初始化差不多，再新增一个而已
        self._push(val)

        # 因为是小根堆，所以每次添加的都会比之前的小，所以第k大就是列表最后一个啦
        return self.HEAP[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


if __name__ == '__main__':
    # obj = KthLargest(k, nums)
    # param_1 = obj.add(val)
    # print(param_1)
    pass
