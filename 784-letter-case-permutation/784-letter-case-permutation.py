class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if s.isnumeric():
            return [s]
        l = list(s)
        n = len(s)
        solution = []
        def backtrack(start):
            if start == n:
                solution.append(self.joinList(l))
            for i in range(start, n):
                if l[i].isalpha():
                    solution.append(self.joinList(l))
                    l[i] = l[i].swapcase()
                    backtrack(i+1)
                    l[i] = l[i].swapcase()
                else:
                    solution.append(self.joinList(l))
        backtrack(0)
        return set(solution)
        
    def joinList(self, l):
        return ''.join(l)