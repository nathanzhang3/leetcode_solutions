class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        all_nums = n * [True]
        all_nums[0:2] = 2 * [False]
        for i in range(2, int(n**0.5) + 1): 
            if all_nums[i]:
                for j in range(i**2, n, i):
                    all_nums[j] = False

        return sum(all_nums) 
