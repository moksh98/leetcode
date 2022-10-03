/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if(root == null) {
            return result;
        }
        while(!queue.isEmpty()) {
            Queue<TreeNode> tempQ = new LinkedList<>();
            List<Integer> val = new ArrayList<>();
            while(!queue.isEmpty()) {
                TreeNode current = queue.poll();
                val.add(current.val);
                if(current.left != null) {
                    tempQ.add(current.left);
                }
                if(current.right != null) {
                    tempQ.add(current.right);
                }
            }
            result.add(val);
            queue = tempQ;
        }
        return result;
    }
}