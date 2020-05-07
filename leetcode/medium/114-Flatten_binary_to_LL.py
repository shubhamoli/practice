"""
    Leetcode #114
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        root.left = None
        root.right = left

        tmp = root
        while tmp.right:
            tmp = tmp.right

        tmp.right = right


    def flatten_dfs(self, root: TreeNode) -> TreeNode:

        if not root:
            return None

        def helper(prev, node):

            prev.right = node
            right = node.right

            prev = node

            if node.left:
                prev = helper(prev, node.left)

            node.left = None

            if right:
                prev = helper(prev, right)

            return prev


        tmp = TreeNode(-1)

        helper(tmp, root)

        return tmp.right


if __name__ == "__main__":


    """
    Expected Tree
        1
       / \
      2   5
     / \   \
    3   4   6
    """

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right = TreeNode(5)
    root.right.right = TreeNode(6)


    def printll(ll):
        while ll:
            print(ll.val, end="->")
            ll = ll.right
        print()

    printll(Solution().flatten_dfs(root))

