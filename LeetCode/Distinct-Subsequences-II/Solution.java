1import java.util.Arrays;
2
3class Solution {
4    public int distinctSubseqII(String s) {
5        int n = s.length();
6        int MOD = 1_000_000_007;
7        
8        // dp[i] stores distinct subsequences of s.substring(0, i) including empty set
9        int[] dp = new int[n + 1];
10        dp[0] = 1; // Base case: empty subsequence
11        
12        // Stores the last 1-based index where each character appeared
13        int[] last = new int[26];
14        Arrays.fill(last, -1);
15        
16        for (int i = 1; i <= n; i++) {
17            char ch = s.charAt(i - 1);
18            
19            // Double the previous number of distinct subsequences
20            dp[i] = (2 * dp[i - 1]) % MOD;
21            
22            // If the character has appeared before, remove duplicate counts
23            if (last[ch - 'a'] != -1) {
24                int prevIdx = last[ch - 'a'];
25                dp[i] = (dp[i] - dp[prevIdx - 1] + MOD) % MOD;
26            }
27            
28            // Update last seen 1-based index for current character
29            last[ch - 'a'] = i;
30        }
31        
32        // Subtract 1 to exclude the empty subsequence
33        return (dp[n] - 1 + MOD) % MOD;
34    }
35}