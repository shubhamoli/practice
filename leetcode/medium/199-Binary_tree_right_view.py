"""
    Leetcode #199
"""


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        queue = []

        queue.append(root)

        while queue:
            size = len(queue)

            for i in range(size):
                curr = queue.pop(0)
                # since we are inserting right first (see below)
                # so i == 0 at each level will give rightmost element
                if i == 0:
                    res.append(curr.val)

                if curr.right:
                    queue.append(curr.right)

                if curr.left:
                    queue.append(curr.left)

        return res


if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)

    root.right = TreeNode(3)
    root.right.right = TreeNode(4)

    assert Solution().rightSideView(root) == [1, 3, 4]

