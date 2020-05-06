"""
    Leetcode #94
"""


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []

        def helper(curr):
            if not curr:
                return

            # Inorder traveral flow
            # left -> root -> right
            helper(curr.left)
            res.append(curr.val)
            helper(curr.right)

        helper(root)
        return res


if __name__ == "__main__":

    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)

    print(Solution().inorderTraversal(tree))    # [1, 3, 2]
