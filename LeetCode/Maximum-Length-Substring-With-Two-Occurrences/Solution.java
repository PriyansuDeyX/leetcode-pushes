1class Solution {
2    public int maximumLengthSubstring(String s) {
3        int[] charCount = new int[26];
4        int left = 0;
5        int maxLen = 0;       
6        for (int right = 0; right < s.length(); right++) {
7            char rightChar = s.charAt(right);
8            charCount[rightChar - 'a']++;
9            
10            while (charCount[rightChar - 'a'] > 2) {
11                char leftChar = s.charAt(left);
12                charCount[leftChar - 'a']--;
13                left++;
14            }          
15            maxLen = Math.max(maxLen, right - left + 1);
16        }    
17        return maxLen;
18    }
19}