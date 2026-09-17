1class Solution:
2    def minSumOfLengths(self, arr: list[int], target: int) -> int:
3        n = len(arr)
4        dp = [float('inf')] * n
5        left = 0
6        current_sum = 0
7        min_ans = float('inf')
8        
9        for right in range(n):
10            current_sum += arr[right]
11            
12            while current_sum > target:
13                current_sum -= arr[left]
14                left += 1
15                
16            if current_sum == target:
17                curr_len = right - left + 1
18                if left > 0 and dp[left - 1] != float('inf'):
19                    min_ans = min(min_ans, curr_len + dp[left - 1])
20                
21                if right > 0:
22                    dp[right] = min(dp[right - 1], curr_len)
23                else:
24                    dp[right] = curr_len
25            else:
26                if right > 0:
27                    dp[right] = dp[right - 1]
28                    
29        return min_ans if min_ans != float('inf') else -1