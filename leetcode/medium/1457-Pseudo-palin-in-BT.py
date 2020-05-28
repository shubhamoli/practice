"""
    Leetcode #1457
"""


import collections
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        res = 0

        def isPalin(curr):
            return sum(v % 2 for v in collections.Counter(curr).values()) < 2

        def helper(node, curr):
            nonlocal res
            if not node:
                return

            curr.append(node.val)
            if not node.left and not node.right:
                if isPalin(curr):
                    res += 1

            helper(node.left, curr)
            helper(node.right, curr)

            curr.pop()

        helper(root, [])
        return res



if __name__ == "__main__":

    solution = Solution()

    def buildTree(nodes: List[int], root, i: int = 0) -> TreeNode:
        if i >= len(nodes):
            return None

        root = TreeNode(nodes[i])
        if root.val:
            root.left = buildTree(nodes, root.left, 2*i+1)
            root.right = buildTree(nodes, root.right, 2*i+2)

        return root

    tree = buildTree([2,3,1,3,1,None,1], None)

    assert solution.pseudoPalindromicPaths(tree) == 2


