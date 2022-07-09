#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-07-09 17:14
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    面试题14：字符串中的变位词.py
# @Project: wrath
# @Package: 
# @Ref: https://leetcode.cn/problems/MPnaiL/

"""
目：输入字符串s1和s2，如何判断字符串s2中是否包含字符串s1的某个变位词？如果字符串s2中包含字符串s1的某个变位词，则字符串s1至少有
一个变位词是字符串s2的子字符串。假设两个字符串中只包含英文小写字母。例如，字符串s1为"ac"，字符串s2为"dgcaf"，由于字符串s2中包
含字符串s1的变位词"ca"，因此输出为true。如果字符串s1为"ab"，字符串s2为"dgcaf"，则输出为false。
"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # 获取两个字符串的长度
        len1, len2 = len(s1), len(s2)
        # 如果需要变位的字符串超过原字符串，则直接返回
        if len1 > len2:
            return False

        # 统计变位次里面每一个字母出现的次数
        map_s1 = Counter(s1)

        # 1. 针对变位词没有移动的情况
        for i in range(len1):
            # 初始化窗口
            if s2[i] in map_s1:
                # 如果原字符串里面有字母在变位次映射表里面，减1
                map_s1[s2[i]] -= 1

            # 获取变位次映射表里卖弄最大的之，看是不是为0，如果是0，说明映射表里面的字母用完了
            if max(list(map_s1.values())) == 0:
                return True

        # 针对变位词不在首位，而是在中间某部分
        for p in range(len1, len2):  # 滑动窗口
            # 从变位次最小长度除考试遍历
            if s2[p] in map_s1:
                # 如果原字符串里面含有，则把对应的字母减去一个
                # 原有保存的事s1的，需要删去s2里面有的
                map_s1[s2[p]] -= 1

            # 滑动窗口往后继续
            if s2[p - len1] in map_s1:

                # 针对s2里面新增的部分，有可能是新增，也有可能是增加
                map_s1[s2[p - len1]] += 1

            if max(list(map_s1.values())) == 0:
                return True

        return False


if __name__ == '__main__':
    print(Solution().checkInclusion(s1="ab", s2="eidbaooo"))
