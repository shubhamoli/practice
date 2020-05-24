"""
    Leetcode #337
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob_naive_DP(sef, root: TreeNode) -> int:
        memo = {}
        def helper(node):
            if not node:
                return 0

            if memo.get(node) is not None:
                return memo.get(node)

            val_left = val_right = 0

            if node.left:
                # as we can't rob root.left (linked to root)
                # we will rob root.left.left
                val_left = max(helper(node.left.left), helper(node.left.right))

            if node.right:
                # same goes for right subtree
                val_right = max(helper(node.right.left), helper(node.right.right))

            val = max(val_left + val_right + node.val, helper(node.left), helper(node.right))

            memo[node] = val

            return val

        return helper(root)


    def rob(self, root: TreeNode) -> int:

        def helper(node):
            if not node:
                return (0, 0) # index 0: rob later, 1: now

            left = helper(node.left)
            right = helper(node.right)

            # if robbing root of subtree now
            # adding node.val
            now = node.val + left[1] + right[1]

            # if skipping root of subtree
            later = max(left) + max(right)

            return (now, later)

        return max(helper(root))


if __name__ == "__main__":

    solution = Solution()

    # build tree from level order traversal
    def buildTree(nodes: List[int], root, i: int = 0) -> TreeNode:
        if i >= len(nodes):
            return None

        root = TreeNode(nodes[i])
        root.left = buildTree(nodes, root.left, 2*i+1)
        root.right = buildTree(nodes, root.right, 2*i+2)

        return root

    root = buildTree([3,2,3,None,3,None,1], None)
    # assert solution.rob(root) == 7

    root = buildTree([3,4,5,1,3,None,1], None)
    # assert solution.rob(root) == 9
