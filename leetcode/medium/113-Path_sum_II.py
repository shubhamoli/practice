"""
    Leetcode #113
"""


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return None

        res = []

        def helper(node, curr, target):
            curr.append(node.val)
            target = target - node.val

            if not node.left and not not.right and target == 0:
                res.append(curr[:])

            if node.left:
                helper(node.left, curr, target)
            if node.right:
                helper(node.right, curr, target)

            tmp = curr.pop()
            target += tmp



        helper(root, [], sum)
        return res


if __name__ == "__main__":


    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    """
    Expected Tree
          5
         / \
        4   8
       /   / \
      11  13  4
     /  \    / \
    7    2  5   1
    """

    print(Solution().pathSum(root, 22))
