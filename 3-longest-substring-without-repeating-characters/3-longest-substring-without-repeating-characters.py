class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start = 0
        end = 1
        max_len = end-start
        while end <= len(s)-1:
            for i in range(start, end):
                if s[i] == s[end]:
                    start = i+1
                    break
            end += 1
            max_len = max_len if max_len > (end-start) else (end-start)
        return max_len