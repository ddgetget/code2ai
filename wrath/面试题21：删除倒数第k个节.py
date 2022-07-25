#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-07-16 19:42
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    面试题21：删除倒数第k个节.py
# @Project: code2ai
# @Package: 
# @Ref:
"""
题目：如果给定一个链表，请问如何删除链表中的倒数第k
个节点？假设链表中节点的总数为n
，那么1≤k
≤n
。要求只能遍历链表一次。
例如，输入图4.1（a）中的链表，删除倒数第2个节点之后的链表如图4.1（b）所
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 题目要求只能遍历一遍，所以双指针，第二个指针线跑n个长度，然后双指针联动，第二个指针跑到末尾，第一个指针的位置就是目标位置
        left = right = head
        # count用于记录便利次数，小于n的原因是从0开始的
        count = 0
        while count < n:
            # 指针不断向后移动
            right = right.next
            # 迭代次数加1
            count += 1

        # 针对链表长度不够n的情况，直接返回链表
        if not right:
            return head.next

        # 当两个指针相聚为n的长度的时候，确保有指针还有值，如果没值，说明遍历完了
        while right.next:
            # 左指针往右移动
            left = left.next
            # 有指针往右移动
            right = right.next
        # 这时候的左指针需要接后后结点
        left.next = left.next.next
        # 返回指针即可
        return head


if __name__ == '__main__':
    print(Solution().removeNthFromEnd(2))
