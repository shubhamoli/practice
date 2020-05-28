"""
    Leetcode #1448
"""


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0

        def helper(node, val):
            nonlocal res
            if not node or node.val is None:
                return 0

            if node.val >= val:
                res += 1

            if node.left:
                helper(node.left, max(node.val, val))

            if node.right:
                helper(node.right, max(node.val, val))


        # root will always be considered a "good node"
        helper(root, root.val)
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

    tree = buildTree([3,1,4,3,None,1,5], None)

    assert solution.goodNodes(tree) == 4

    tree = buildTree([3,3,None,4,2], None)

    assert solution.goodNodes(tree) == 3    # Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
