"""
    Leetcode #102
"""


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []

        queue = [root]
        while queue:
            n = len(queue)
            tmp = []

            # pop first "n" element (all of same level level)
            for i in range(n):
                curr = queue.pop(0)

                tmp.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            res.append(tmp)

        return res


if __name__ == "__main__":

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Solution().levelOrder(root))      # [ [3], [9, 20], [15, 7] ]
