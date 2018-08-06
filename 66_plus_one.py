class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        up = 1
        new_digits = []
        
        for i in range(1, len(digits) + 1):
            if up:
                if digits[-i] + 1 == 10:
                    new_digits.insert(0, 0)
                    if i == len(digits):
                        new_digits.insert(0, 1)
                        up = 0
                else:
                    new_digits.insert(0, digits[-i] + 1)
                    up = 0
            else:
                new_digits.insert(0, digits[-i])
        return new_digits