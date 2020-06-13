"""
    Leetcode #101
"""

from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric_RECUR(self, root: TreeNode) -> bool:
        if not root:
            return False

        def helper(l, r):
            if l and r:
                return l.val == r.val and helper(l.left, r.right) and helper(l.right, r.left)

            return l == r

        return helper(root.left, root.right)


    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = deque([(root.left, root.right),])

        while queue:
            l, r = queue.popleft()

            if not l and not r:
                continue

            if not l or not r:
                return False

            if l.val != r.val:
                return False

            queue.append((l.left, r.right))
            queue.append((l.right, r.left))

        return True


if __name__ == "__main__":

    solution = Solution()

    def buildTree(nums: List[int], root: TreeNode, i: int = 0) -> TreeNode:
        if i >= len(nums):
            return None

        root = TreeNode(nums[i])
        root.left = buildTree(nums, root.left, 2*i+1)
        root.right = buildTree(nums, root.left, 2*i+2)

        return root

    root = buildTree([1,2,2,3,4,4,3], None)
    assert solution.isSymmetric(root) == True
    assert solution.isSymmetric_RECUR(root) == True

    root = buildTree([1,2,2,None,3,None,3], None)
    assert solution.isSymmetric(root) == False
    assert solution.isSymmetric_RECUR(root) == False
