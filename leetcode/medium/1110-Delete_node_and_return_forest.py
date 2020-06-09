"""
    Leetcode #1110
"""


from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        res = []
        to_delete = set(to_delete)

        if root not in to_delete:
            res.append(root)

        def helper(node):
            if not node:
                return

            node.left = helper(node.left)
            node.right = helper(node.right)

            if node.val in to_delete:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)

                return None

            return node

        root = helper(root)
        if root:
            res.append(root)

        return res


if __name__ == "__main__":

    solution = Solution()

    def buildTree(nums, root, i: int = 0):
        if i >= len(nums):
            return

        root = TreeNode(nums[i])
        if root.val:
            root.left = buildTree(nums, root.left, 2*i + 1)
            root.right = buildTree(nums, root.left, 2*i + 2)

        return root

    root = buildTree([1,2,3,4,5,6,7], None)

    # assert solution.delNodes(root, [3, 5]) == [[1,2,None,4],[6],[7]]
