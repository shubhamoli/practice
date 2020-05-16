"""
    Leetcode 230
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return 0

        i = 0
        for val in self.inorder(root):
            # k-1 because i is starting from 0
            if i == k-1:
                return val
            else:
                i += 1

    def inorder(self, root):
        if not root:
            return

        yield from self.inorder(root.left)
        yield root.val
        yield from self.inorder(root.right)




if __name__ == "__main__":

    solution = Solution()

    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.left.right = TreeNode(2)
    root1.right = TreeNode(4)


    assert solution.kthSmallest(root1, 1) == 1

    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.left.left = TreeNode(2)
    root2.left.left.left = TreeNode(1)

    root2.left.right = TreeNode(4)
    root2.right = TreeNode(6)

