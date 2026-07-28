1from collections import Counter
2
3class Solution:
4    def smallestPalindrome(self, s: str) -> str:
5        #String-er prottekta character kobar ache seta gunbo (frequency count korchi)
6        count = Counter(s)
7        
8        half = []
9        odd_char = ""
10        
11        #Alphabetical order-e (a theke z) sort kore loop chalacchi jate lexicographically smallest pai
12        for char in sorted(count.keys()):
13            freq = count[char]
14            #Proti bar character-gulo ke adha kore first half-e add korchi
15            half.append(char * (freq // 2))
16            #Jodi kono character-er count odd hoy, tahole take majhkane rakhar jonno store korchi
17            if freq % 2 != 0:
18                odd_char = char
19                
20        first_half = "".join(half)
21        
22        #First half, majher odd character (jodi thake),r first half-er ulto (reversed) version judhe palindrome baniye dicchi
23        return first_half + odd_char + first_half[::-1]