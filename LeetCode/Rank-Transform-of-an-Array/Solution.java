1
2class Solution {
3    public int[] arrayRankTransform(int[] arr) {
4        int[] sorted = arr.clone();
5        Arrays.sort(sorted);
6        
7        Map<Integer, Integer> rankMap = new HashMap<>();
8        int rank = 1;
9        
10        for (int num : sorted) {
11            if (!rankMap.containsKey(num)) {
12                rankMap.put(num, rank++);
13            }
14        }
15        
16        int[] result = new int[arr.length];
17        for (int i = 0; i < arr.length; i++) {
18            result[i] = rankMap.get(arr[i]);
19        }
20        
21        return result;
22    }
23}