class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_hash = {}
        for i in s1:
            s1_hash[i] = s1_hash.get(i, 0) + 1
        s1_len = len(s1)
        s2_hash = {}
        start = 0
        for i in range(len(s2)):
            s2_hash[s2[i]] = s2_hash.get(s2[i], 0) + 1
            if i < s1_len-1:
                continue
            if s1_hash == s2_hash:
                return True
            s2_hash[s2[start]] -= 1
            if s2_hash[s2[start]] == 0:
                del s2_hash[s2[start]]
            start += 1
        return False