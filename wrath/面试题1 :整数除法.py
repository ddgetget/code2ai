#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-07-09 13:28
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    面试题1 :整数除法.py
# @Project: wrath
# @Package: 
# @Ref: https://leetcode.cn/problems/xoh6Oh/

"""
题目：输入2个int型整数，它们进行除法计算并返回商，要求不得使用乘号'*'、除号'/'及求余符号'%'。当发生溢出时，返回最大的整数值。假设除数不
为0。例如，输入15和2，输出15/2的结果，即7。
"""


class Solution:
    def divide(self, a: int, b: int) -> int:
        ret = 0
        # 针对除完之后正负判断
        flag = False if (a > 0 and b > 0) or (a < 0 and b < 0) else True
        a, b = abs(a), abs(b)

        def calc(x, y):
            n = 1
            # 1. 被除数首先得大于除数左偏移一位，才能继续
            while x > y << 1:
                # 除数左偏移一位
                y <<= 1
                # n偏移之后是 1 2 4 8
                n <<= 1
            # 返回满足条件且都偏移，即除以2的结果
            return n, y

        # 只要被除数大于除数，还需要继续获取最大接近，但是无法再扩列的数字cnt
        # 【注意】cnt每次循环回来凑是从1开始，不断尝试最大企鹅不超过被除数的那个值
        while a >= b:
            # 调用上面被除数减半的函数，其实被除数val和cnt是不断相向逼近的过程
            cnt, val = calc(a, b)
            ret += cnt
            a -= val

        # 如果是亿昊，还需要体检符号，因为计算的时候都是当做正数进行的
        ret = -ret if flag else ret
        # 针对结果大于数据类型范围的，返回最大范围之-1,因为最大范围那个值是无法正常显示的
        return ret - 1 if ret >= 2 ** 31 else ret


if __name__ == '__main__':
    print(Solution().divide(1, 2))
