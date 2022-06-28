class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        solution = []
        def backtrack(combination, start, k):
            if k == 0:
                solution.append(combination.copy())
            for i in range(start, n+1):
                combination.append(i)
                backtrack(combination, i+1, k-1)
                combination.pop(len(combination)-1)
        backtrack([], 1, k)
        return solution