#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-07-11 08:05
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    面试题79：所有子集.py
# @Project: wrath
# @Package: 
# @Ref:
"""
题目：输入一个不含重复数字的数据集合，请找出它的所有子集。例如，数据集合[1，2]有4个子集，分别是[]、[1]、[2]和[1，2]。
"""
from typing import List


class Solution:
    """
    根据题的意思应该是组合
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result = []

        path = []

        def backtrace(idx):
            # 终止条件,整个集合已经遍历完毕，相当于for循环写非递归的那个
            if idx == length:
                # 收集叶子结点
                result.append(path[:])
                return

            # 单层逻辑，
            # 不添加当前值，即叶子左节点
            backtrace(idx + 1)

            path.append(nums[idx])

            # 添加当前值，即叶子右结点
            backtrace(idx + 1)

            # 回溯 12 13 14 最后一个才有地方存储
            path.pop()

        backtrace(0)
        return result


if __name__ == '__main__':
    print(Solution().subsets(nums=[1, 2, 3]))
