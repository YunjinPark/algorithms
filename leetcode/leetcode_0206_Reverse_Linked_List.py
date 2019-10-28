# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList_1(self, head: ListNode) -> ListNode:
        """ time: O(N), space: O(N)
            input 바꾸지 않고 새롭게 노드를 생성
            iterative
        """
        p, node = head, None

        while (p):
            tmp = ListNode(p.val)
            tmp.next = node
            node = tmp
            p = p.next

        return node

    def reverseList_2(self, head: ListNode) -> ListNode:
        """ time: O(N), space: O(1)
        in place
        iterative"""
        if not head or not head.next: return head

        a = head
        b = head.next
        a.next = None

        while (a and b):
            n = a
            a = b
            b = b.next
            a.next = n
        return a