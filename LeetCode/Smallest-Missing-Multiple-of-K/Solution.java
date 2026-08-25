1import java.util.HashSet;
2import java.util.Set;
3
4public class Solution {
5    public int missingMultiple(int[] nums, int k) {
6        Set<Integer> set = new HashSet<>();
7        for (int num : nums) if (num % k == 0) set.add(num);
8        
9        int target = k;
10        while (set.contains(target)) target += k;
11        return target;
12    }
13}