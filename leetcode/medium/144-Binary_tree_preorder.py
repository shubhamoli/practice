"""
    Leetcode #144
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(node):
            if not node:
                return

            res.append(node.val)
            helper(node.left)
            helper(node.right)

        helper(root)
        print(res)
        return res

    def preorderTraversal_ITER(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = []
        res = []
        q.append(root)

        while q:
            curr = q.pop(0)

            res.append(curr.val)

            tmp = []

            if curr.left:
                tmp.append(curr.left)
            if curr.right:
                tmp.append(curr.right)

            # add item in front of queue
            q = tmp + q

        return res



if __name__ == "__main__":

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)


    assert Solution().preorderTraversal_ITER(root) == [1, 2, 3]
