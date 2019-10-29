# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        time:O(N+M) space:O(N+M)
        stack 이용
        """

        s1, s2, p1, p2 = [], [], l1, l2
        while (p1):
            s1.append(p1.val)
            p1 = p1.next
        while (p2):
            s2.append(p2.val)
            p2 = p2.next

        carry, res = 0, None
        while (s1 or s2):
            tmp_1 = 0 if not s1 else s1.pop()
            tmp_2 = 0 if not s2 else s2.pop()
            s = tmp_1 + tmp_2 + carry
            node = ListNode(s % 10)
            node.next = res
            carry = s // 10
            res = node

        if carry:
            node = ListNode(carry)
            node.next = res
            res = node
        return res

    def addTwoNumbers_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        time:O(N+M) space:O(1)
        """
        p1, s1 = l1, 0
        while (p1):
            s1 = s1 * 10 + p1.val
            p1 = p1.next

        p2, s2 = l2, 0
        while (p2):
            s2 = s2 * 10 + p2.val
            p2 = p2.next

        s = str(s1 + s2)
        node = ListNode(0)
        p = node

        for i in range(0, len(s)):
            p.next = ListNode(int(s[i]))
            p = p.next
        return node.next