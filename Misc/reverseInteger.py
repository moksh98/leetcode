# Leetcode Question 7

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -self.reverseDigit(abs(x))
        elif x > 0:
            return self.reverseDigit(x)
        else:
            return 0
    def reverseDigit(self, x):
        rev = 0
        while x > 0:
            rev = (rev*10) + x%10
            x = x//10
        if rev < (-2 ** 31) or rev > ((2 ** 31) - 1):
            return 0
        return rev