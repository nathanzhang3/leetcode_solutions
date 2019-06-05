class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroPos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[zeroPos], nums[i] = nums[i], nums[zeroPos]
                zeroPos += 1
