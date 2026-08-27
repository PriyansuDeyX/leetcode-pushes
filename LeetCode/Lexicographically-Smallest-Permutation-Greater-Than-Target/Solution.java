1import java.util.Arrays;
2
3public class Solution {
4    public String lexGreaterPermutation(String s, String target) {
5        int n = s.length();
6        int[] sCount = new int[26];
7        for (char c : s.toCharArray()) {
8            sCount[c - 'a']++;
9        }
10
11        // Try to match target[0...i-1] exactly, and make position i strictly larger
12        for (int i = n - 1; i >= 0; i--) {
13            int[] currentCount = sCount.clone();
14            boolean possible = true;
15
16            // Check if s has enough characters to match target[0...i-1]
17            for (int j = 0; j < i; j++) {
18                int charIdx = target.charAt(j) - 'a';
19                if (currentCount[charIdx] > 0) {
20                    currentCount[charIdx]--;
21                } else {
22                    possible = false;
23                    break;
24                }
25            }
26
27            if (!possible) continue;
28
29            // Find the smallest char strictly greater than target[i]
30            int targetCharIdx = target.charAt(i) - 'a';
31            int nextCharIdx = -1;
32            for (int c = targetCharIdx + 1; c < 26; c++) {
33                if (currentCount[c] > 0) {
34                    nextCharIdx = c;
35                    break;
36                }
37            }
38
39            // If a valid character is found, construct the answer
40            if (nextCharIdx != -1) {
41                StringBuilder sb = new StringBuilder();
42                sb.append(target, 0, i);
43                sb.append((char) ('a' + nextCharIdx));
44                currentCount[nextCharIdx]--;
45
46                // Append all remaining characters in ascending (lexicographical) order
47                for (int c = 0; c < 26; c++) {
48                    while (currentCount[c] > 0) {
49                        sb.append((char) ('a' + c));
50                        currentCount[c]--;
51                    }
52                }
53                return sb.toString();
54            }
55        }
56
57        return "";
58    }
59}