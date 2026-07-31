1from collections import Counter
2
3class Solution:
4    def minimumPushes(self, word: str) -> int:
5        counts = Counter(word).most_common()
6        
7        total_pushes = 0
8        for index, (char, freq) in enumerate(counts):
9            presses = (index // 8) + 1
10            total_pushes += freq * presses
11            
12        return total_pushes