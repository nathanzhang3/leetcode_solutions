class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #num = set(range(len(nums)+1)) - set(nums)
        #return next(iter(num))
        return len(nums)*(len(nums)+1)//2 - sum(nums)
