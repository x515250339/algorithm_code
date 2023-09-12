from typing import List


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next
        return l[::-1]


node = ListNode(1, ListNode(2, ListNode(3)))

print(Solution().reversePrint(node))
