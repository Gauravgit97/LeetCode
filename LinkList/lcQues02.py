'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode(0)
        reman = 0
        temp = res
        while l1 and l2:
            val = l1.val + l2.val
            val =val + reman
            if val>=10:
                reman = val //10
                val = val % 10
            else:
                reman = 0
            new_list = ListNode(val)
            temp.next = new_list
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            val = l1.val
            val =val + reman
            if val>=10:
                reman = val //10
                val = val % 10
            else:
                reman = 0
            new_list = ListNode(val)
            temp.next = new_list
            temp = temp.next
            l1 = l1.next

        while l2:
            val = l2.val
            val =val + reman
            if val>=10:
                reman = val //10
                val = val % 10
            else:
                reman = 0
            new_list = ListNode(val)
            temp.next = new_list
            temp = temp.next
            l2 = l2.next
        if reman:
            new_list = ListNode(reman)
            temp.next = new_list
            temp = temp.next

        return res.next
            