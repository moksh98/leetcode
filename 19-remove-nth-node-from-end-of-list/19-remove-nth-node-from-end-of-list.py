# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         length = 0
#         start = head
#         while start != None:
#             start = start.next
#             length += 1
#         if n == length:
#             return head.next
#         k = length - n
#         count = 0
#         start = head
#         while count <= k:
#             if count == k-1:
#                 start.next = start.next.next
#                 count += 1
#             else:
#                 start = start.next
#                 count += 1
#         return head

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = head
        back = head
        for i in range(n):
            front = front.next
        if front == None:
            return head.next
        while front.next != None:
            front = front.next
            back = back.next
        back.next = back.next.next
        return head
            