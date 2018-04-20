# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2 = 0
        p = l1
        i = 1
        while p:
            g = p.val
            p = p.next
            num1 += g * i
            i *= 10

        p = l2
        i = 1
        while p:
            g = p.val
            p = p.next
            num2 += g * i
            i *= 10

        num = num1 + num2
        res = []
        while num >= 10:
            res.append(num % 10)
            num //= 10

        res.append(num % 10)
        return res