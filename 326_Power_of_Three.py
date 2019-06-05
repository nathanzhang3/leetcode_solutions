class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n / 3 == 1:
            return True
        elif n % 3 == 0 and n / 3 > 1:
            return self.isPowerOfThree(n/3)
        else:
            return False
