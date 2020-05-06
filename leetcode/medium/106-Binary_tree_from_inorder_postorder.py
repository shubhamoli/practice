"""
    Leetcode #106
"""


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None


        store = {}
        for i in range(len(inorder)):
            store[inorder[i]] = i

        def helper(low, high):
            if low > high:
                return None

            node = TreeNode(postorder[index])
            self.index -= 1

            mid = store.get(node.val)

            node.right = helper(post+1, high)
            node.left = helper(low, post-1)

            return node

        self.index = len(postorder) - 1
        return helper(0, len(postorder) - 1)


if __name__ == "__main__":

    ino = [9,3,15,20,7]
    post = [9,15,7,20,3]

    Solution().buildTree(ino, post)


    """
    Expected Tree
        3
       / \
      9  20
        /  \
       15   7
    """
