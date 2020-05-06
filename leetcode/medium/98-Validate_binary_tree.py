"""
    Leetcode #98
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode, lower=float("-inf"), upper=float("inf")) -> bool:

        if not root:
            return True

        # if out of bounds return False
        if root.val <= lower or root.val >= upper:
            return False

        # for left node, root.val is upper bound
        # means left subtree can't be greater than root
        left = self.isValidBST(root.left, lower, root.val)

        # for right node, root.val is lower bound
        # means right subtree can't be lower than root
        right = self.isValidBST(root.right, root.val, upper)

        return (left and right)



if __name__ == "__main__":

    solution = Solution()


    tree1 = TreeNode(2)
    tree1.left = TreeNode(1)
    tree1.right = TreeNode(3)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)

    tree3 = TreeNode(3)
    tree3.right = TreeNode(2)
    tree3.right.right = TreeNode(1)

    tree4 = TreeNode(1)
    tree4.right = TreeNode(2)
    tree4.right.right = TreeNode(3)

    assert solution.isValidBST(tree1) == True
    assert solution.isValidBST(tree2) == False
    assert solution.isValidBST(tree3) == False
    assert solution.isValidBST(tree4) == True

