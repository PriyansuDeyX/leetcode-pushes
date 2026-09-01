1import java.util.ArrayDeque;
2import java.util.Arrays;
3import java.util.Deque;
4
5class Solution {
6
7    private static class State {
8
9        int r, c, mask, energy, moves;
10
11        State(int r, int c, int mask, int energy, int moves) {
12            this.r = r;
13            this.c = c;
14            this.mask = mask;
15            this.energy = energy;
16            this.moves = moves;
17        }
18    }
19
20    public int minMoves(String[] classroom, int energy) {
21        int rows = classroom.length;
22        int cols = classroom[0].length();
23
24        int startR = -1, startC = -1;
25        int litterCount = 0;
26        int[][] litterIndex = new int[rows][cols];
27        for (int[] row : litterIndex) {
28            Arrays.fill(row, -1);
29        }
30        for (int r = 0; r < rows; r++) {
31            for (int c = 0; c < cols; c++) {
32                char ch = classroom[r].charAt(c);
33                if (ch == 'S') {
34                    startR = r;
35                    startC = c;
36                } else if (ch == 'L') {
37                    litterIndex[r][c] = litterCount++;
38                }
39            }
40        }
41
42        int targetMask = (1 << litterCount) - 1;
43
44        int[][][] bestEnergy = new int[rows][cols][1 << litterCount];
45        for (int i = 0; i < rows; i++) {
46            for (int j = 0; j < cols; j++) {
47                Arrays.fill(bestEnergy[i][j], -1);
48            }
49        }
50
51        Deque<State> queue = new ArrayDeque<>();
52        queue.offer(new State(startR, startC, 0, energy, 0));
53        bestEnergy[startR][startC][0] = energy;
54
55        int[][] dirs = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
56
57        while (!queue.isEmpty()) {
58            State curr = queue.poll();
59
60            if (curr.mask == targetMask) {
61                return curr.moves;
62            }
63
64            if (curr.energy == 0) {
65                continue;
66            }
67
68            for (int[] dir : dirs) {
69                int nr = curr.r + dir[0];
70                int nc = curr.c + dir[1];
71
72                if (
73                    nr >= 0 &&
74                    nr < rows &&
75                    nc >= 0 &&
76                    nc < cols &&
77                    classroom[nr].charAt(nc) != 'X'
78                ) {
79                    char cellType = classroom[nr].charAt(nc);
80
81                    int nextMask = curr.mask;
82                    if (cellType == 'L') {
83                        nextMask |= (1 << litterIndex[nr][nc]);
84                    }
85
86                    int nextEnergy = (cellType == 'R')
87                        ? energy
88                        : curr.energy - 1;
89
90                    if (nextEnergy > bestEnergy[nr][nc][nextMask]) {
91                        bestEnergy[nr][nc][nextMask] = nextEnergy;
92                        queue.offer(
93                            new State(
94                                nr,
95                                nc,
96                                nextMask,
97                                nextEnergy,
98                                curr.moves + 1
99                            )
100                        );
101                    }
102                }
103            }
104        }
105
106        return -1;
107    }
108}