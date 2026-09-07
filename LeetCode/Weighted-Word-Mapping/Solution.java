1class Solution {
2    public String mapWordWeights(String[] words, int[] weights) {
3        StringBuilder result = new StringBuilder();
4        for (String word : words) {
5            int totalWeight = 0;
6            for (char ch : word.toCharArray()) {
7                totalWeight += weights[ch - 'a'];
8            }
9            int remainder = totalWeight % 26;
10            char mappedChar = (char) ('z' - remainder);
11            result.append(mappedChar);
12        }
13        return result.toString();
14    }
15}