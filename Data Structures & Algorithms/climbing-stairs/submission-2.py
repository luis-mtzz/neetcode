class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        one_step, two_step = 2, 1
        for i in range(3, n + 1):
            current_step = one_step + two_step
            two_step = one_step
            one_step = current_step
        return current_step