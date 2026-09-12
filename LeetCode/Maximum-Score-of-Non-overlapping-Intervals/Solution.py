1import bisect
2import functools
3import math
4
5class Solution:
6    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
7        indexed_intervals = sorted((*interval, i) for i, interval in enumerate(intervals))
8        
9        @functools.lru_cache(None)
10        def dp(i: int, quota: int):
11            if i == len(indexed_intervals) or quota == 0:
12                return 0, ()
13            
14            skip_weight, skip_selected = dp(i + 1, quota)
15            
16            _, r, weight, original_index = indexed_intervals[i]
17            j = bisect.bisect_right(indexed_intervals, (r, math.inf))
18            next_weight, next_selected = dp(j, quota - 1)
19            
20            pick_weight = weight + next_weight
21            pick_selected = tuple(sorted((original_index, *next_selected)))
22            
23            if pick_weight > skip_weight or (pick_weight == skip_weight and pick_selected < skip_selected):
24                return pick_weight, pick_selected
25            return skip_weight, skip_selected
26
27        return list(dp(0, 4)[1])