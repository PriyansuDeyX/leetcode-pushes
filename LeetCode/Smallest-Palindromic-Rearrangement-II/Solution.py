1from collections import Counter
2from math import comb
3
4class Solution:
5    def smallestPalindrome(self, s: str, k: int) -> str:
6        LIMIT = 10**6 + 1
7
8        # Count character frequencies
9        freq = Counter(s)
10
11        half_count = Counter()
12        middle = ""
13
14        for ch in freq:
15            half_count[ch] = freq[ch] // 2
16            if freq[ch] % 2 == 1:
17                middle = ch
18
19        half_len = sum(half_count.values())
20
21        # Count number of distinct permutations
22        def count_permutations(counter):
23            total = sum(counter.values())
24            ans = 1
25            rem = total
26
27            for v in counter.values():
28                if v > 0:
29                    ans *= comb(rem, v)
30                    if ans > LIMIT:
31                        return LIMIT
32                    rem -= v
33            return ans
34
35        # Not enough palindromes
36        if count_permutations(half_count) < k:
37            return ""
38
39        first_half = []
40
41        for _ in range(half_len):
42            for ch in sorted(half_count.keys()):
43                if half_count[ch] == 0:
44                    continue
45
46                half_count[ch] -= 1
47                ways = count_permutations(half_count)
48
49                if ways >= k:
50                    first_half.append(ch)
51                    break
52                else:
53                    k -= ways
54                    half_count[ch] += 1
55
56        first_half = "".join(first_half)
57        return first_half + middle + first_half[::-1]