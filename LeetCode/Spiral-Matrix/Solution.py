1from typing import List
2
3class Solution:
4    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
5        result = []
6        if not matrix:
7            return result
8        
9        # Define the initial boundaries
10        top, bottom = 0, len(matrix) - 1
11        left, right = 0, len(matrix[0]) - 1
12        
13        # Continue spiraling as long as boundaries haven't crossed
14        while top <= bottom and left <= right:
15            
16            # 1. Traverse left to right along the top row
17            for i in range(left, right + 1):
18                result.append(matrix[top][i])
19            top += 1 # Shrink top boundary
20            
21            # 2. Traverse top to bottom along the right column
22            for i in range(top, bottom + 1):
23                result.append(matrix[i][right])
24            right -= 1 # Shrink right boundary
25            
26            # Check if boundaries have crossed after first half of the spiral
27            if top <= bottom:
28                # 3. Traverse right to left along the bottom row
29                for i in range(right, left - 1, -1):
30                    result.append(matrix[bottom][i])
31                bottom -= 1 # Shrink bottom boundary
32                
33            if left <= right:
34                # 4. Traverse bottom to top along the left column
35                for i in range(bottom, top - 1, -1):
36                    result.append(matrix[i][left])
37                left += 1 # Shrink left boundary
38                
39        return result
40        