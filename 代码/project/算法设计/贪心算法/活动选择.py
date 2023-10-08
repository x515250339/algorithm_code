"""
活动选择问题
假设有n个活动，这些活动要占用同一片场地，而场地在某时
刻只能供一个活动使用。
每个活动都有一个开始时间s和结束时间f（题目中时间以整数
表示）,表示活动在[s，f)区间占用场地。
问：安排哪些活动能够使该场地举办的活动的个数最多？
"""
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]

activities.sort(key=lambda x: x[1])


def activate_selection(active):
    """
    时间复杂度：O(n)
    空间复杂度：O(n)

    :param active:
    :return:
    """
    res = [active[0]]
    for i in range(1, len(active)):
        if active[i][0] >= res[-1][1]:
            res.append(active[i])
    return res


if __name__ == '__main__':
    print(activate_selection(activities))
