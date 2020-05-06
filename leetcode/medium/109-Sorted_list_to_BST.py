"""
    Leetcode #109
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        aux = []
        node = head

        while node:
            aux.append(node.val)
            node = node.next

        def helper(start, end):
            if start > end:
                return None

            # left to middle will always be left node
            # right to middle will always be right node
            # since it sorted, we'll get a BST
            mid = (start+end) // 2

            node = TreeNode(aux[mid])

            node.left = helper(start, mid-1)
            node.right = helper(mid+1, end)

            return node

        return helper(0, len(aux) - 1)


if __name__ == "__main__":

