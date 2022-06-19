class Solution:
    def reverseWords(self, s: str) -> str:
        rev = ""
        s += ' '
        temp = ""
        for i in range(len(s)):
            if s[i] != ' ':
                temp += s[i]
            else:
                rev += self.reverse(temp) +  ' '
                temp = ""
        return rev.strip()
    def reverse(self, s):
        l = list(s)
        start = 0;
        end = len(l)-1
        while start < end:
            l[start], l[end] = l[end], l[start]
            start += 1
            end -= 1
        return ''.join(l)