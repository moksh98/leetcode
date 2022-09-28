class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        total = 0
        one_before = 2
        two_before = 1
        for i in range(2, n):
            total = one_before + two_before
            two_before = one_before
            one_before = total
        return total