#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-07-11 16:21
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    面试题47：二叉树剪枝.py
# @Project: wrath
# @Package: 
# @Ref:
"""
题目：一棵二叉树的所有节点的值要么是0要么是1，请剪除该二叉树中所有节点的值全都是0的子树。例如，在剪除图8.2（a）中二叉树中所有节点值都为0的子树之后的结果如图8.2（b）所示
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    观察发现他叶子结点全是0，跟也是0，就需要删除，后序遍历已经把所有的值都看到了，比较容易实现
    """

    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.left == None and root.right == None and root.val == 0:
            # 返回None就是把叶子结点删了，并且当前根节点为None，也已经没了
            return None

        return root



if __name__ == '__main__':
    print(Solution().pruneTree(root=[1, None, 0, 0, 1]))
