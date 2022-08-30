"""
1534 · 将二叉搜索树转换为已排序的双向链接列表
算法
中等
通过率
72%
题目
题解
笔记
讨论
排名
记录
描述
将BST转换为已排序的循环双向链表。可以将左右指针视为双向链表中上一个和下一个指针的同义词。

我们以下面的BST为例，它可以帮助您更好地理解问题：

bstdlloriginalbst

我们希望将此BST转换为循环双向链表。双向链表中的每个节点都有一个前任和后继。对于循环双向链表，第一个元素的前导是最后一个元素，最后一个元素的后继是第一个元素。

下图显示了上述BST的循环双向链表。“head”符号表示它指向的节点是链表的最小元素。

bstdllreturndll

具体来说，我们希望进行转型。转换后，树节点的左指针应指向其前一个指针，右指针应指向其后继指针。我们应该将指针返回到链表的第一个元素。

下图显示了转换后的BST。实线表示后继关系，而虚线表示前趋关系。

bstdllreturnbst

背完这套刷题模板，真的不一样！

北大学霸令狐冲15年刷题经验总结的《算法小抄模板Cheat Sheet》助你上岸！

微信添加【jiuzhang0607】备注【小抄】领取


样例
样例 1:

输入: {4,2,5,1,3}
        4
       /  \
      2   5
     / \
    1   3
输出: "left:1->5->4->3->2  right:1->2->3->4->5"
解释:
left：逆序输出
right：正序输出
样例 2:

输入: {2,1,3}
        2
       /  \
      1   3
输出: "left:1->3->2  right:1->2->3"
标签
"""


class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next


class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """

    def treeToDoublyList(self, root):
        dfs = []
        self.dfs(root, dfs)
        if not dfs:
            return None

        head, prev = None, None

        for val in dfs:
            node = DoublyListNode(val)
            if head is None:
                head = node
            else:
                prev.next = node
            node.prev = prev
            prev = node
        return head

    def dfs(self, root, res_list):
        if root:
            self.dfs(root.left, res_list)
            res_list.append(root.val)
            self.dfs(root.right, res_list)
        return


from leetcode.utils.util import makeTree
res = Solution().treeToDoublyList(makeTree([3, 1, 2]))
print(res.val)
print(res.next.val)
print(res.next.next.val)