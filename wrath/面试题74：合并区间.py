#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-07-10 10:26
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    面试题74：合并区间.py
# @Project: wrath
# @Package: 
# @Ref: https://leetcode.cn/problems/SsGoHC/

"""
题目：输入一个区间的集合，请将重叠的区间合并。每个区间用两个数字比较，分别表示区间的起始位置和结束位置。例如，输入区间
[[1，3]，[4，5]，[8，10]，[2，6]，[9，12]，[15，18]]，合并重叠的区间之后得到[[1，6]，[8，12]，[15，18]]。

"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # print(sorted(intervals))
        # 先进行按区间头排序
        sorted_intervals = sorted(intervals)

        result = []
        for sorted_interval in sorted_intervals:
            if not result or result[-1][1] < sorted_interval[0]:
                # 对第一个完全在第二个前面，不存在交叉
                # [2, 6], [8, 10]，这种情况无法合并，成为新的数组
                result.append(sorted_interval)
            else:
                # 对于最后一个值，需要不断更新成最大值
                # [1, 3], [2, 6]这种值，说明有交叉，获取最大值就是合并
                result[-1][1] = max(result[-1][1], sorted_interval[1])

        return result


if __name__ == '__main__':
    print(Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
