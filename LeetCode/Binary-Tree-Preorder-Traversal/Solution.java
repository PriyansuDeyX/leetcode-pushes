1/**
2 * Definition for a binary tree node.
3 * public class TreeNode {
4 *     int val;
5 *     TreeNode left;
6 *     TreeNode right;
7 *     TreeNode() {}
8 *     TreeNode(int val) { this.val = val; }
9 *     TreeNode(int val, TreeNode left, TreeNode right) {
10 *         this.val = val;
11 *         this.left = left;
12 *         this.right = right;
13 *     }
14 * }
15 */
16import java.util.ArrayList;
17import java.util.List;
18
19/**
20 * Definition for a binary tree node.
21 * public class TreeNode {
22 *     int val;
23 *     TreeNode left;
24 *     TreeNode right;
25 *     TreeNode() {}
26 *     TreeNode(int val) { this.val = val; }
27 *     TreeNode(int val, TreeNode left, TreeNode right) {
28 *         this.val = val;
29 *         this.left = left;
30 *         this.right = right;
31 *     }
32 * }
33 */
34class Solution {
35    public List<Integer> preorderTraversal(TreeNode root) {
36        List<Integer> result = new ArrayList<>();
37        dfs(root, result);
38        return result;
39    }
40
41    private void dfs(TreeNode node, List<Integer> result) {
42        if (node == null) return;
43        
44        result.add(node.val);     // Process Root
45        dfs(node.left, result);   // Traverse Left
46        dfs(node.right, result);  // Traverse Right
47    }
48}