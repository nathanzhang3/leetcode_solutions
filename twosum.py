class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == None or target == None:
            return None
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length, 1):
                if nums[i] + nums[j] == target:
                    return [i, j]