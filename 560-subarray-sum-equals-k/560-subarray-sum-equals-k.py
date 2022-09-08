# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         mapping = {}
#         current_sum = 0
#         count = 0
#         mapping[0] = 1 
#         for num in nums:
#             current_sum += num
#             if current_sum-k in mapping.keys():
#                 count += mapping[current_sum-k]
#             mapping[current_sum] = mapping.get(current_sum, 0) + 1
#         return count

from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        d=defaultdict(int)
        count, currsum=0,0
        for i in nums:
            currsum+=i
            count+=d[currsum-k]
            d[currsum]+=1
        count+=d[k]
        return count