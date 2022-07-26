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
#
#  Related Topics 递归 链表 数学 👍 8401 👎 0


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_tmp = 0
        ln1 = ln2 = ListNode()
        while l1 or l2:
            sum_tmp += l1.val if l1 else 0
            sum_tmp += l2.val if l2 else 0
            ln2.next = ListNode(sum_tmp % 10)
            ln2 = ln2.next
            sum_tmp = sum_tmp // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if sum_tmp:
            ln2.next = ListNode(sum_tmp)
        return ln1.next


l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
print(Solution().addTwoNumbers(l1, l2))
