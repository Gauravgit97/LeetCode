'''21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.'''

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        rlist = ListNode()
        temp = rlist
        while list1 != None and list2 != None:
            if list1.val<list2.val:
                rlist.next = list1
                list1 = list1.next
            else:
                rlist.next = list2
                list2 = list2.next
            rlist = rlist.next
        
        while list1 !=None:
            rlist.next = list1
            return temp.next

        while list2 !=None:
            rlist.next = list2
            return temp.next
        
        return temp.next