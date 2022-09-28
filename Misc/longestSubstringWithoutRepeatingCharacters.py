# Leetcode Question 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        else:
            substring = ""
            maxLen = 0
            left = 0
            right = 0
            while right < len(s):
                if s[right] not in substring:
                    substring += s[right]
                    right += 1
                else:
                    maxLen = len(substring) if maxLen < len(substring) else maxLen
                    for i in range(left, right, 1):
                        if s[i] == s[right]:
                            left = i + 1
                            break
                    substring = s[left:right+1]
                    right += 1
            return max(maxLen, len(substring))