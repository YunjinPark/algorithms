# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs_1(self, head):
        """
        time: O(N), space: O(1)
        """
        res = ListNode(0)
        res.next = head
        p = res

        while (p.next and p.next.next):
            a, b = p.next, p.next.next
            a.next, b.next = b.next, a
            p.next = b
            p = a

        return res.next

    def swapPairs_2(self, head):
        """
        time: O(N), space: O(N)
        새로운 노드 생성해서 함.
        """
        res = ListNode(0)
        p_out = res
        p_in = head
        while (p_in and p_in.next):
            p_out.next = ListNode(p_in.next.val)
            p_out.next.next = ListNode(p_in.val)
            p_in = p_in.next.next
            p_out = p_out.next.next
        if p_in: p_out.next = ListNode(p_in.val)

        return res.next