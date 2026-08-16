1import java.util.LinkedList;
2import java.util.Queue;
3
4class Solution {
5    public int minDepth(TreeNode root) {
6        if (root == null) {
7            return 0;
8        }
9        
10        Queue<TreeNode> queue = new LinkedList<>();
11        queue.offer(root);
12        int depth = 1;
13        
14        while (!queue.isEmpty()) {
15            int levelSize = queue.size();
16            for (int i = 0; i < levelSize; i++) {
17                TreeNode current = queue.poll();
18                
19                // Return immediately upon reaching the first leaf node
20                if (current.left == null && current.right == null) {
21                    return depth;
22                }
23                
24                if (current.left != null) {
25                    queue.offer(current.left);
26                }
27                if (current.right != null) {
28                    queue.offer(current.right);
29                }
30            }
31            depth++;
32        }
33        
34        return depth;
35    }
36}