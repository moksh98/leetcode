# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        prev_node = head
        next_node = head
        while next_node is not None:
            if count == 0:
                next_node = head.next
                head.next = None
                count += 1
            else:
                head = next_node
                next_node = head.next
                head.next = prev_node
                prev_node = head
        return head
                
            