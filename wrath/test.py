#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-07-09 15:29
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    test.py
# @Project: wrath
# @Package: 
# @Ref:
from collections import Counter


def test_left_calc(a=10, b=1):
    """
    左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。
    :param a:
    :param b:
    :return:
    """
    print(a << b)


def test_Counter(s):
    """
    统计字符串里面每一个字母出现的次数
    :param s:
    :return:
    """
    map_s1 = Counter(s)
    print(map_s1)


def test_ord(a):
    print(ord(a))


if __name__ == '__main__':
    # test_left_calc(a=64, b=1)
    # test_Counter(s="hadjkshdka")
    test_ord(a='a')