1import java.util.Arrays;
2import java.util.ArrayList;
3import java.util.List;
4
5class Solution {
6    public int[][] merge(int[][] intervals) {
7        if (intervals.length <= 1) {
8            return intervals;
9        }
10
11        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
12
13        List<int[]> result = new ArrayList<>();
14        int[] currentInterval = intervals[0];
15        result.add(currentInterval);
16
17        for (int[] interval : intervals) {
18            int currentEnd = currentInterval[1];
19            int nextStart = interval[0];
20            int nextEnd = interval[1];
21
22            if (currentEnd >= nextStart) {
23                currentInterval[1] = Math.max(currentEnd, nextEnd);
24            } else {
25                currentInterval = interval;
26                result.add(currentInterval);
27            }
28        }
29
30        return result.toArray(new int[result.size()][]);
31    }
32}