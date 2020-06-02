"""
    Leetcode #237
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# only access to a node is given
# no head nothing
class Solution:
    def deleteNode(self, node):
        if node.next == None:
            return

        node.val = node.next.val
        node.next = node.next.next


