# Leetcode Question 8

import re
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        pattern = '^(-?|\+?)[0-9]+'
        ans = re.search(pattern, s)
        if ans == None: 
            return 0
        elif int(ans.group()) < -2**31:
            return -2**31
        elif int(ans.group()) > (2**31 - 1):
            return (2**31 - 1)
        else:
            return int(ans.group())