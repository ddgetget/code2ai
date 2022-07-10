#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-07-10 14:32
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    面试题68：查找插入位置.py
# @Project: wrath
# @Package: 
# @Ref: https://leetcode.cn/problems/N6YdxV/
"""
题目：输入一个排序的整数数组nums和一个目标值t
，如果数组nums中包含t
，则返回t
在数组中的下标；如果数组nums中不包含t
，则返回将t
按顺序插入数组nums中的下标。假设数组中没有相同的数字。例如，输入数组nums为[1，3，6，8]，如果目标值t
为3，则输出1；如果t
为5，则返回2。
"""
from typing import List


class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 初始化左边界和右边界
        left, right = 0, len(nums) - 1
        # 只要左边界小于等于右边界均可进行二分查找当左边界大于右边界时显然当前要查找的值不在数组中
        while left <= right:
            # 数组元素个数可能为奇数，取整除
            md = (left + right) // 2
            # 若当前二分查找的中间位置元素刚好是要找的，直接返回
            if nums[md] == target:
                return md
            # 否则，若中间位置的元素大于目标值，则应当从较小的一半数组中查找，故右边界更新为md-1
            # 由于md本身大于target，故不需要考虑md位置的元素，所以是md-1
            elif nums[md] > target:
                right = md - 1
            # 同理，若中间位置元素小于目标值，应当从较大的一半数组中查找，故更新左边界为md+1
            else:
                left = md + 1
        # 左边界即为待插入的位置
        return left


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 初始化左边界和右边界
        left, right = 0, len(nums) - 1
        # 只要左边界小于等于右边界均可进行二分查找当左边界大于右边界时显然当前要查找的值不在数组中
        while left <= right:
            # 数组元素个数可能为奇数，取整除
            md = (left + right) // 2
            # 若当前二分查找的中间位置元素刚好是要找的，直接返回
            if nums[md]>=target:
                if md==0 or nums[md-1]<target:
                    return md
                right = md - 1
            # 同理，若中间位置元素小于目标值，应当从较大的一半数组中查找，故更新左边界为md+1
            else:
                left = md + 1
        # 左边界即为待插入的位置
        return len(nums)

if __name__ == '__main__':
    print(Solution().searchInsert(nums=[1, 3, 5, 6], target=4))
    print(Solution().searchInsert(nums=[1, 3, 5, 6], target=2))
