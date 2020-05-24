"""
    Leetcode #1008
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return none

        root = TreeNode(preorder[0])

        stack = [root]

        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)

        return root


if __name__ == "__main__":

    def printInoder(root):
        if not root:
            return

        printInoder(root.left)
        print(root.val)
        printInoder(root.right)


    printInoder(Solution().bstFromPreorder([8,5,1,7,10,12]))

