/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        Map<ListNode, Integer> visited = new HashMap<ListNode, Integer>();
        int count = 0;
        while(head != null) {
            ListNode next = head;
            if(visited.getOrDefault(next, null) != null) {
                return next;
            }
            visited.put(next, count);
            count += 1;
            head = head.next;
        }
        return null;
    }
}