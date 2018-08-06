class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = list(sorted(set(nums)))
        return len(nums)
