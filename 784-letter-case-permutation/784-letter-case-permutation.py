class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        solution = []
        def backtrack(string, index):
            if len(string) == n:
                solution.append(string)
                return
            backtrack(string+s[index], index+1)
            if s[index].isalpha():
                backtrack(string+s[index].swapcase(), index+1)
        backtrack('', 0)
        return solution

class Solution2:
    def letterCasePermutation(self, s: str) -> List[str]:
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