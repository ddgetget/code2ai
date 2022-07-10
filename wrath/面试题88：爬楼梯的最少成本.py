#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-07-10 08:12
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    面试题88：爬楼梯的最少成本.py
# @Project: wrath
# @Package: 
# @Ref: https://leetcode.cn/problems/GzCJIP/

"""
题目：一个数组cost的所有数字都是正数，它的第i
个数字表示在一个楼梯的第i
级台阶往上爬的成本，在支付了成本cost[i
]之后可以从第i
级台阶往上爬1级或2级。假设台阶至少有2级，既可以从第0级台阶出发，也可以从第1级台阶出发，请计算爬上该楼梯的最少成本。例如，输入数组
[1，100，1，1，100，1]，则爬上该楼梯的最少成本是4，分别经过下标为0、2、3、5的这4级台阶，如图14.1所示。
"""
from typing import List


class Solution1:
    """
    缺陷：对于递归问题，拆解的小问题，并没有进行缓存，导致多次重复计算相同结果，会出现时间过长问题
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        首先问题是求解个数，所以选择动态规划。
        动态规划又分为两种方法：
        方法一：自上而下，采用递归求解，优化点，对之前已求解的小问题存储下来，方便下次直接查询
        方法二：自下而上，便利求解，只用到前两个直，所以存储空间可以优化到长度为2
        :param cost: 每一步花费的代价
        :return: 总花费金额
        """
        # 获取楼梯的长度
        length = len(cost)
        # 大问题拆解成两个小问题
        return min(self.helper(cost, length - 2), self.helper(cost, length - 1))

    def helper(self, cost, i):
        # 递归函数，求解上一步或上上一步与当前步之和的最小值
        # 递归终止条件
        if i < 2: return cost[i]
        # 递归的转换函数
        return min(self.helper(cost, i - 2), self.helper(cost, i - 1)) + cost[i]


class Solution2:
    """
    缺陷：对于递归问题，拆解的小问题，并没有进行缓存，导致多次重复计算相同结果，会出现时间过长问题
    优化：分配一块存储空间，对小步骤进行查询
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        首先问题是求解个数，所以选择动态规划。
        动态规划又分为两种方法：
        方法一：自上而下，采用递归求解，优化点，对之前已求解的小问题存储下来，方便下次直接查询
        方法二：自下而上，便利求解，只用到前两个直，所以存储空间可以优化到长度为2
        :param cost: 每一步花费的代价
        :return: 总花费金额
        """
        # 获取楼梯的长度
        length = len(cost)

        dp = [0 for _ in range(length)]
        # 大问题拆解成两个小问题
        self.helper(cost, length - 1, dp)

        # 只需要对最后两个值判断那个最小
        return min(dp[length - 2], dp[length - 1])

    def helper(self, cost, i, dp):
        # 递归函数，求解上一步或上上一步与当前步之和的最小值
        if i < 2:
            #     # 递归终止的时候
            #     dp[i] = cost[i]  # 这种情况容易出错，当输入之后两个值的时候，dp[1]=cost[1],dp[0]=0,然后最小值是0，
            #     忽略了dp[1]的值，没有给新的
            dp[0] = cost[0]
            dp[1] = cost[1]

        elif dp[i] == 0:
            # 递归部分，比如计算到第9步，发现没有dp[9]的结果，所以需要计算第8和第7步的结果，然后计算第9步的结果并存取
            self.helper(cost, i - 2, dp)  # 假设已知。方便计算第i步骤
            self.helper(cost, i - 1, dp)  # 假设已知，方便计算第i步骤
            # 一个小目标进行存储，方便下次查询，节省时间
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]  # 基于上面两行假设，直接获取第i步结果，即前i步最小花费


class Solution3:
    """
    缺陷：缓存空间太大，可以节省一下
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        首先问题是求解个数，所以选择动态规划。
        动态规划又分为两种方法：
        方法一：自上而下，采用递归求解，优化点，对之前已求解的小问题存储下来，方便下次直接查询
        方法二：自下而上，便利求解，只用到前两个直，所以存储空间可以优化到长度为2
        :param cost: 每一步花费的代价
        :return: 总花费金额
        """
        length = len(cost)
        dp = [0 for _ in range(length)]
        # 初始化第一个值
        dp[0] = cost[0]
        # 初始化第二个值
        dp[1] = cost[1]

        for i in range(2, length):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]

        return min(dp[length - 2], dp[length - 1])

class Solution:
    """
    缺陷：缓存空间太大，可以节省一下
    优化：对存储空间压缩到两个
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        首先问题是求解个数，所以选择动态规划。
        动态规划又分为两种方法：
        方法一：自上而下，采用递归求解，优化点，对之前已求解的小问题存储下来，方便下次直接查询
        方法二：自下而上，便利求解，只用到前两个直，所以存储空间可以优化到长度为2
        :param cost: 每一步花费的代价
        :return: 总花费金额
        """
        length = len(cost)
        dp = [0 for _ in range(2)]
        # 初始化第一个值
        dp[0] = cost[0]
        # 初始化第二个值
        dp[1] = cost[1]

        for i in range(2, length):
            dp[i%2] = min(dp[0], dp[1]) + cost[i]

        return min(dp[0], dp[1])

if __name__ == '__main__':
    print(Solution().minCostClimbingStairs(cost=[1, 100]))
    print(Solution().minCostClimbingStairs(cost=[10, 15, 20]))
