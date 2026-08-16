1class Solution {
2    public boolean stoneGameIX(int[] stones) {
3        int cnt0 = 0, cnt1 = 0, cnt2 = 0;
4        for (int stone : stones) {
5            int rem = stone % 3;
6            if (rem == 0) cnt0++;
7            else if (rem == 1) cnt1++;
8            else cnt2++;
9        }
10        
11        if (cnt0 % 2 == 0) {
12            return cnt1 >= 1 && cnt2 >= 1;
13        } else {
14            return Math.abs(cnt1 - cnt2) > 2;
15        }
16    }
17}