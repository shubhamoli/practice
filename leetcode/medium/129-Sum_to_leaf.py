"""
    Leetcode #129
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        def helper(node, curr):
            if not node:
                return 0

            curr = (curr*10) + node.val

            # leaf encountered
            # return sum of this path
            if not node.left and not node.right:
                return curr

            return helper(node.left, curr) + helper(node.right, curr)

        return helper(root, 0)


if __name__ == "__main__":


    """
    Tree
        4
       / \
      9   0
     / \
    5   1
    """
    root = TreeNode(4)

    root.left = TreeNode(9)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    root.right = TreeNode(0)

    assert Solution().sumNumbers(root) == 1026

    root = TreeNode(0)
    root.left = TreeNode(1)

    assert Solution().sumNumbers(root) == 1

    # ll = [4, 9, 0, 5, 1]

