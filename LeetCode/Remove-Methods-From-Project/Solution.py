1from collections import deque
2from typing import List
3
4class Solution:
5    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
6        # Step 1: Build the adjacency list
7        graph = [[] for _ in range(n)]
8        for u, v in invocations:
9            graph[u].append(v)
10            
11        # Step 2: Find all methods reachable from k (suspicious methods)
12        suspicious = [False] * n
13        queue = deque([k])
14        suspicious[k] = True
15        
16        while queue:
17            curr = queue.popleft()
18            for neighbor in graph[curr]:
19                if not suspicious[neighbor]:
20                    suspicious[neighbor] = True
21                    queue.append(neighbor)
22                    
23        # Step 3: Check if any non-suspicious method invokes a suspicious method
24        is_isolated = True
25        for u, v in invocations:
26            if not suspicious[u] and suspicious[v]:
27                is_isolated = False
28                break
29                
30        # Step 4: Return remaining methods or all methods based on isolation check
31        if not is_isolated:
32            return list(range(n))
33            
34        return [i for i in range(n) if not suspicious[i]]