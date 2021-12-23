class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            zigzag = ['']*numRows
            row = 0
            ch = 1
            zigzag[0] += s[0]
            while True:
                while row != numRows:
                    if ch == len(s):
                        break
                    if row == 0:
                        row += 1
                    zigzag[row] += s[ch]
                    ch += 1
                    row += 1
                while row > 0:
                    if ch == len(s):
                        break
                    if row == numRows:
                        row -= 2
                    else:
                        row -= 1
                    zigzag[row] += s[ch]
                    ch += 1
                if ch == len(s):
                    break
            return ''.join(zigzag)