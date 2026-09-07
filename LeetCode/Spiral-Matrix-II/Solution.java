1class Solution {
2    public int[][] generateMatrix(int n) {
3        int[][] matrix = new int[n][n];
4        
5        int top = 0;
6        int bottom = n - 1;
7        int left = 0;
8        int right = n - 1;
9        
10        int num = 1;
11        
12        while (top <= bottom && left <= right) {
13            for (int i = left; i <= right; i++) {
14                matrix[top][i] = num++;
15            }
16            top++;
17    
18            for (int i = top; i <= bottom; i++) {
19                matrix[i][right] = num++;
20            }
21            right--;
22            if (top <= bottom) {
23                for (int i = right; i >= left; i--) {
24                    matrix[bottom][i] = num++;
25                }
26                bottom--;
27            }
28            
29            if (left <= right) {
30                for (int i = bottom; i >= top; i--) {
31                    matrix[i][left] = num++;
32                }
33                left++;
34            }
35        }
36        
37        return matrix;
38    }
39}