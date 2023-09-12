# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
#  请你将两个数相加，并以相同形式返回一个表示和的链表。
#
#  你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
#
#
#  示例 1：
#
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#
#
#  示例 2：
#
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
#
#  示例 3：
#
#
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#
#
#
#
#  提示：
#
#
#  每个链表中的节点数在范围 [1, 100] 内
#  0 <= Node.val <= 9
#  题目数据保证列表表示的数字不含前导零
#
#  Related Topics 递归 链表 数学 👍 8425 👎 0


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        sum_tmp = 0
        r = n = ListNode()

        while l1 or l2:
            sum_tmp += l1.val if l1 else 0
            sum_tmp += l2.val if l2 else 0
            n.next = ListNode(sum_tmp % 10)
            sum_tmp //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if sum_tmp:
            n.next = ListNode(sum_tmp)
        return r.next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print(Solution().addTwoNumbers(l1, l2).val)
print(Solution().addTwoNumbers(l1, l2).next.val)
print(Solution().addTwoNumbers(l1, l2).next.next.val)

# for i in '807':
#     int(i) % 10
