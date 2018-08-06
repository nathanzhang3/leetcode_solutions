class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 2:
            return 1
        else:
            one_step_back = 1
            two_step_back = 1
            
            for i in range(n-1):
                this_step = one_step_back + two_step_back
                two_step_back = one_step_back
                one_step_back = this_step
            return this_step