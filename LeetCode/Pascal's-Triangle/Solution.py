1class Solution:
2    def generate(self, numRows: int) -> list[list[int]]:
3        triangle = []
4        
5        for i in range(numRows):
6            row = [1] * (i + 1)
7            for j in range(1, i):
8                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
9                
10            triangle.append(row)
11            
12        return triangle