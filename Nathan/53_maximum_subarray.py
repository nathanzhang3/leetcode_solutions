class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = nums[0]
        for i in range(len(nums)-1):
            if nums[i] > 0:
                nums[i+1] += nums[i]
            if nums[i+1] > max_num:
                max_num = nums[i+1]
        return max_num