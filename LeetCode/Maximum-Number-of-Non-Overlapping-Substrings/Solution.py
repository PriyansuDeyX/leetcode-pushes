1class Solution:
2
3  def maxNumOfSubstrings(self, s: str) -> List[str]:
4    n = len(s)
5    left = [n] * 26
6    right = [0] * 26
7
8    # Step 1: Record first and last occurrence of each character
9    for i, ch in enumerate(s):
10      idx = ord(ch) - ord('a')
11      left[idx] = min(left[idx], i)
12      right[idx] = i
13
14    intervals = []
15
16    # Step 2: Validate and expand intervals for each unique starting character
17    for i in range(n):
18      if i != left[ord(s[i]) - ord('a')]:
19        continue
20
21      end = right[ord(s[i]) - ord('a')]
22      valid = True
23      j = i
24      while j <= end:
25        ch_idx = ord(s[j]) - ord('a')
26        if left[ch_idx] < i:
27          valid = False
28          break
29        end = max(end, right[ch_idx])
30        j += 1
31
32      if valid:
33        intervals.append((i, end))
34
35    # Step 3: Greedy interval selection to avoid overlap and minimize length
36    intervals.sort(key=lambda x: x[1])
37    res = []
38    prev_end = -1
39
40    for start, end in intervals:
41      if start > prev_end:
42        res.append(s[start : end + 1])
43        prev_end = end
44      else:
45        # If a smaller valid interval is nested inside the previous one, replace it
46        if end < prev_end:
47          res[-1] = s[start : end + 1]
48          prev_end = end
49
50    return res