"""
    Leetcode #236
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            None

        def helper(node):
            if not node or node == p or node == q:
                return node

            left = helper(node.left)
            right = helper(node.right)

            if not left:
                return right

            if not right:
                return left

            return node

        return helper(root)


if __name__ == "__main__":

    arr = [3,5,1,6,2,0,8,None,None,7,4]

    tree = tmp = None
    for i in range(len(arr)):
        node = TreeNode(arr[i])
        if 2*i+1 < len(arr):
            node.left = TreeNode(arr[2*i+1])
        if 2*i+2 < len(arr):
            node.right = TreeNode(arr[2*i+2])


    def helper(root):

        if not root: return

        helper(root.left)
        print(root)
        helper(root.right)


    helper(root)

    assert Solution().lowestCommonAncestor(root, 5, 1) == 3
    assert Solution().lowestCommonAncestor(root, 5, 4) == 5
    assert Solution().lowestCommonAncestor(root, 0, 7) == 3
