1from collections import Counter
2
3class Solution:
4    def minimumPushes(self, word: str) -> int:
5        # Sob character-er count ba kobar ase ta ber kortchi
6        cnt = Counter(word)
7        
8        ans = 0
9        # Jegulo besi bar ase, ogula age rakhbo (descending order-e sort korchi)
10        sorted_freqs = sorted(cnt.values(), reverse=True)
11        
12        # Greedy vabe press calculate korchi
13        for i, freq in enumerate(sorted_freqs):
14            # Prothom 8 ta key te 1 bar, tarporer 8 , 2 bar, emon kore barbe
15            presses = i // 8 + 1
16            ans += presses * freq
17            
18        return ans