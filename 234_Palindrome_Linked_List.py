# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        nums = [head.val]
        next = head.next
        while next:
            nums.append(next.val)
            next = next.next
        for i in range(int(len(nums)/2)):
            if nums[i] != nums[-i-1]:
                return False
        return True
