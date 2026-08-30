1class Solution {
2    public int minimumDeletions(int[] nums) {
3        int n = nums.length;
4        if (n <= 2) return n;
5
6        int minIdx = 0, maxIdx = 0;
7        for (int i = 1; i < n; i++) {
8            if (nums[i] < nums[minIdx]) minIdx = i;
9            if (nums[i] > nums[maxIdx]) maxIdx = i;
10        }
11
12        int left = Math.min(minIdx, maxIdx);
13        int right = Math.max(minIdx, maxIdx);
14
15        int op1 = right + 1;
16        int op2 = n - left;
17        int op3 = (left + 1) + (n - right);
18
19        return Math.min(op1, Math.min(op2, op3));
20    }
21}