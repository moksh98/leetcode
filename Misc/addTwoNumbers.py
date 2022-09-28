# Leetcode Question 2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.sumTwoNumbers(l1, l2, 0)
    
    def sumTwoNumbers(self, l1, l2, carry):
        if l1 == None and l2 == None and carry == 0:
            return None
        else:
            num1 = 0 if l1 == None else l1.val
            l1 = None if l1 == None else l1.next
            
            num2 = 0 if l2 == None else l2.val
            l2 = None if l2 == None else l2.next
            
            sum = num1 + num2 + carry
            carry = sum // 10
            return ListNode(sum - carry*10, self.sumTwoNumbers(l1, l2, carry))