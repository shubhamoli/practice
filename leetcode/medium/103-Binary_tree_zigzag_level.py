"""
    Leetcode #103
"""


from typing import List
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []

        queue = deque([(root, 0)])
        res = defaultdict(deque)

        while queue:
            node, level = queue.popleft()

            if node:
                if level % 2 == 0:
                    res[level].append(node.val)
                else:
                    res[level].appendleft(node.val)

            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))

        result = []
        for k, v in res.items():
            result.append(list(v))

        return result


if __name__ == "__main__":

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Solution().zigzagLevelOrder(root))      # [ [3], [20, 9], [15, 7] ]
