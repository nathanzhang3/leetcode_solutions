# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None
        this = head
        while this != None:
            helperNext = this.next
            this.next = last
            last = this
            this = helperNext
        return last
