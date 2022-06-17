# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        bad_version = 0
        while start <= end:
            mid = (start+end)//2
            if isBadVersion(mid) == False:
                start = mid+1
            elif isBadVersion(mid):
                bad_version = mid
                end = mid-1
        return bad_version