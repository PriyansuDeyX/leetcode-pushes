1import java.util.Arrays;
2
3class Solution {
4    public long findKthSmallest(int[] coins, int k) {
5        long minCoin = coins[0];
6        for (int c : coins) {
7            minCoin = Math.min(minCoin, c);
8        }
9
10        long low = 1;
11        long high = minCoin * k;
12        long result = high;
13
14        while (low <= high) {
15            long mid = low + (high - low) / 2;
16            if (countMultiples(coins, 0, 1, 0, mid) >= k) {
17                result = mid;    
18                high = mid - 1;
19            } else {
20                low = mid + 1;   
21            }
22        }
23
24        return result;
25    }
26
27    private long countMultiples(int[] coins, int index, long currentLcm, int subsetSize, long target) {
28        if (index == coins.length) {
29            if (subsetSize == 0) return 0;
30            long count = target / currentLcm;
31            return (subsetSize % 2 == 1) ? count : -count;
32        }
33        long totalCount = countMultiples(coins, index + 1, currentLcm, subsetSize, target);
34        long newLcm = lcm(currentLcm, coins[index]);
35        
36        if (newLcm <= target) {
37            totalCount += countMultiples(coins, index + 1, newLcm, subsetSize + 1, target);
38        }
39
40        return totalCount;
41    }
42    private long gcd(long a, long b) {
43        return b == 0 ? a : gcd(b, a % b);
44    }
45    private long lcm(long a, long b) {
46        return (a / gcd(a, b)) * b;
47    }
48}