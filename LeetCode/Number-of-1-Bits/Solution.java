1class Solution {
2    public int hammingWeight(int n) {
3        int count = 0;
4        while (n != 0) {
5            n &= (n - 1); // Clears the lowest set bit
6            count++;
7        }
8        return count;
9    }
10}