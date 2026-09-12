1class Solution:
2    def getRow(self, rowIndex: int) -> list[int]:
3        row = [1]
4        
5        for j in range(1, rowIndex + 1):
6            
7            next_val = row[-1] * (rowIndex - j + 1) // j
8            row.append(next_val)
9            
10        return row
11