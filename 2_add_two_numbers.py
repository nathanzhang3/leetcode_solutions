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
        l3 =  ListNode(l1.val + l2.val)
        node = l3
        res = 0
        
        while l1 or l2 or res:
            if l1:
                v1 = l1.val
                l1 = l1.next 
            else:
                v1 = 0
                
            if l2:
                v2 = l2.val
                l2 = l2.next 
            else:
                v2 = 0
            
            nodes_sum = v1 + v2 + res
            
            node.next = ListNode(nodes_sum % 10)
            res = nodes_sum // 10
            
            node = node.next
            
        return l3.next