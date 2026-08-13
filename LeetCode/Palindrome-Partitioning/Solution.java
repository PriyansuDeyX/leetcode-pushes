1import java.util.*;
2class Solution {
3    public List<List<String>> partition(String s) {
4        List<List<String>> res = new ArrayList<>();
5        dfs(0, s, new ArrayList<>(), res);
6        return res;
7    }
8
9    private void dfs(int start, String s, List<String> path, List<List<String>> res) {
10        if (start == s.length()) res.add(new ArrayList<>(path));
11        for (int end = start; end < s.length(); end++) {
12            if (isPal(s, start, end)) {
13                path.add(s.substring(start, end + 1));
14                dfs(end + 1, s, path, res);
15                path.remove(path.size() - 1);
16            }
17        }
18    }
19
20    private boolean isPal(String s, int i, int j) {
21        while (i < j) if (s.charAt(i++) != s.charAt(j--)) return false;
22        return true;
23    }
24}