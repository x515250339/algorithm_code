from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 先给定一个最小值和最大值
        min_price = prices[0]
        max_profit = 0
        # 根据题意，我们需要顺序查询，遍历每一天的价格
        for price in prices:
            # 取最大 当前价格-最小价格 和 最高价格做比较
            # max_profit = max(price - min_price, max_profit)
            # 另一种写法，当交易差值比目前最大值大 则重新赋值
            if max_profit < price - min_price:
                max_profit = price - min_price
            # 取最小 当前价格 和 最小价格
            # min_price = min(price, min_price)
            # 同上
            if min_price > price:
                min_price = price
        # 返回交易最大的
        return max_profit


print(Solution().maxProfit([2, 9, 1, 9, 7]))
