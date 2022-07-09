#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-07-09 16:34
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    面试题6：排序数组中的两个数字之和.py
# @Project: wrath
# @Package: 
# @Ref: https://leetcode.cn/problems/JFETK5/

"""
题目：输入一个递增排序的数组和一个值k
，请问如何在数组中找出两个和为k
的数字并返回它们的下标？假设数组中存在且只存在一对符合条件的数字，同时一个数字不能使用两次。例如，输入数组[1，2，4，6，10]，k
的值为8，数组中的数字2与6的和为8，它们的下标分别为1与3。
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        针对反向相反的，保持只和不变即可。
        如果大了，肯定是右边的需要左移，这样保持和变小。
        如果和变小了，肯定是左边的需要往右边移动，因为指针从左到右递增。

        针对同方向的，常用来处理数组中子数组的和或者乘积。
        若果大于目标值，需要移动第一个指针。（这里知识有个约定，两个指针同方向，是有前后区别的）
        如果小于目标值，需要移动第二个指针。

        :param numbers: 有序数组
        :param target: 目标值
        :return:
        """

        # 首先获取两个索引
        begin, end = 0, len(numbers) - 1

        # 双指针只要相对位置没有发生变化，就一直循环
        while begin < end:
            # 分三种情况，若满足
            if numbers[begin] + numbers[end] == target:
                # 返回结果，看样子也是列表
                return [begin, end]
            # 针对之和小于目标值，理论上是移动左边较小的一方，这样才能使和相对增大
            elif (numbers[begin] + numbers[end]) < target:
                # 所以移动左边的指针
                begin += 1
            else:
                # 其他情况，也是技术大于目标值，需要只恨左移
                end -= 1


if __name__ == '__main__':
    print(Solution().twoSum(numbers=[1, 2, 4, 6, 10], target=8))
