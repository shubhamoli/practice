"""
    Leetcode #222
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        curr = root
        left_height = 1
        while curr.left:
            left_height += 1
            curr = curr.left

        curr = root
        right_height = 1
        while curr.right:
            right_height += 1
            curr = curr.right

        if left_height == right_height:
            return 2 ** left_height - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(3)
    root.right.left = TreeNode(6)

    assert Solution().countNodes(root) == 6

