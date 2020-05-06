"""
    Leetcode #95
"""


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n < 1:
            return []

        self.res = []

        def helper(left, right):
            if left >= right:
                return [None]

            nodes = []
            for i in range(left, right):
                leftNodes = helper(left, i)
                rightNodes = helper(i+1, right)
                for l in leftNodes:
                    for r in rightNodes:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        nodes.append(node)
            return nodes

        return helper(1, n+1)


if __name__ == "__main__":

    solution = Solution()

    assert len(solution.generateTrees(3)) == 5
