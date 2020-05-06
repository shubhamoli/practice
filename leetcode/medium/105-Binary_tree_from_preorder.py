"""
    Leetcode #105
"""


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        store = {}
        for i in range(len(inorder)):
            store[inorder[i]] = i

        def helper(low, high):
            if low > high:
                return None

            node = TreeNode(preorder[self.ind])
            # increase index for next iteration
            self.ind += 1

            # index of inorder will act as mid
            # by definition (left->root->right) of inorder traversal
            # left (mid-1) of a node is node.left
            # right (mid+1) of it is node.right
            mid = map_inorder[node.val]

            node.left = helper(low, mid-1)
            node.right = helper(mid+1, high)

            return node

        return helper(0, len(inorder)-1)



if __name__ == "__main__":

    pre = [3,9,20,15,7]
    ino = [9,3,15,20,7]

    Solution().buildTree(pre, ino)

    """
    Expected Tree
        3
       / \
      9  20
        /  \
       15   7

    """
