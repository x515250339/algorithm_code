"""
一个小偷在某个商店发现有n个商品,第i个商品价值v元,重w千克。他希望 拿走的价值尽量高,但他的背包最多只能容纳W千克的东西。他应该拿走哪些 商品?
0-1背包:对于一个商品,小偷要么把它完整拿走,要么留下下。不能只拿走 一部分,或把一个商品拿走多次。(商品为金条)
分数背包（贪心算法）:对于一个商品,小偷可以拿走其中任意一部分。 (商品为金砂)
"""
goods = [(60, 10), (120, 30), (100, 20)]
# 倒序排列 价格由低倒高
goods.sort(key=lambda x: x[0] / x[1], reverse=True)
print(goods)


def fractional_backpack(goods, w):
    """
    时间复杂度：O(n)
    空间复杂度：O(n)
    解法：分数背包
    """
    # 计算可以取的容量
    m = [float("inf") for _ in range(len(goods))]
    # 计算取走总价格
    total = 0
    for i, (price, weight) in enumerate(goods):
        # 当前重量小于总重量
        if weight <= w:
            # 全部取走
            m[i] = 1
            # 重量相应减
            w -= weight
            # 拿走价格总数增加
            total += price
        else:
            # 剩余格子不够，则能取多少取多少
            m[i] = w / weight
            # 价格为取走的*价格
            total += m[i] * price
            break
    return total, m


print(fractional_backpack(goods, 50))
