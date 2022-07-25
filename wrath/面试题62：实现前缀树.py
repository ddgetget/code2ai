#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-07-11 11:04
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    面试题62：实现前缀树.py
# @Project: wrath
# @Package: 
# @Ref: https://leetcode.cn/problems/QC3q1f/
"""
题目：请设计实现一棵前缀树Trie，它有如下操作。
·函数insert，在前缀树中添加一个字符串。
·函数search，查找字符串。如果前缀树中包含该字符串，则返回true；否则返回false。
·函数startWith，查找字符串前缀。如果前缀树中包含以该前缀开头的字符串，则返回true；否则返回false
"""


class Trie1():
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie1()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 声明一个节点的数据类型，包含一个节点，以及他是否是单次结尾的点，其实每一个点都有一个这样的isWord
        self.child = dict()
        self.isWord = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # 首先获取这棵树本身
        root = self
        # 遍历每一个字符
        for c in word:
            # 针对当前字符不在这棵树的子节点上
            if c not in root.child:
                # 创造一个新的节点，然后和之前的节点连起来
                root.child[c] = Trie()
            # 根节点移动到之前的孩子结点，孩子结点成为新的根节点，然后继续循环，知道把最后一个字符也放到这棵树上。
            root = root.child[c]
        # 之后添加完记得把最后一个节点的标志位改一下，不然查询的时候走到这一步，系统不认为它是已经存在的
        root.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # 在查询的时候，首先拿到这棵树
        root = self
        # 然后遍历每一个字符
        for c in word:
            # 针对字符不在这个孩子结点上
            if c not in root.child:
                # 那说明之前没有插入过，也及时说系统诶呦当前词语
                return False
            # 如果当前字符在当前孩子结点上，当前根节点需要移动到孩子结点，继续进行搜索
            root = root.child[c]
        # 已经遍历完所有的字符，需要判断是不是之前添加的时候，是有结尾标志符，这里直接返回root.isWord也是可以的
        return root.isWord == True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # 查询前缀是不是在里面，也需要先拿到这棵树
        root = self
        # 同理遍历字符串
        for c in prefix:
            # 针对字符不在字符串里面，直接返回就可以了
            if c not in root.child:
                return False
            # 每次需要移动到下一个孩子结点，更新成根节点
            root = root.child[c]
        # 如果所有字符都跑完了，那么就说明这个字符串有一条路径存在这棵树上，所以肯定是正确的
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == '__main__':
    trie = Trie()
    print(trie.insert("apple"))
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    print(trie.insert("app"))
    print(trie.search("app"))
