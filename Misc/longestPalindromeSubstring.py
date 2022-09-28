class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.checkPalindrome(0, len(s)-1, s)
        
    def checkPalindrome(self, left, right, s):
        substr = s[left:right+1]
        if substr == substr[::-1]:
            return substr
        else:
            return max(self.checkPalindrome(left+1, right, s), self.checkPalindrome(left, right-1, s), key=lambda x: len(x))

sol = Solution()
print(sol.longestPalindrome("abbcccbbabcaaccbababcbcabca"))