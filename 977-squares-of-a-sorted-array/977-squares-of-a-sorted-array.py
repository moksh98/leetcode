class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new_list = [0] * n
        start = 0
        index = n - 1
        end = n - 1
        while start <= end:
            if abs(nums[start]) > abs(nums[end]):
                new_list[index] = nums[start]*nums[start]
                start += 1
            else:
                new_list[index] = nums[end]*nums[end]
                end -= 1
            index -= 1
        return new_list