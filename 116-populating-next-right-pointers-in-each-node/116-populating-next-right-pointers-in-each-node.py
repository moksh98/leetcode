"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        queue = [root]
        temp = []
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left is not None and node.right is not None:
                temp.append(node.left)
                temp.append(node.right)
            if len(queue) == 0:
                node.next = None
                queue = temp
                temp = []
            else:
                node.next = queue[0]
        return root