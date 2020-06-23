"""
    Leetcode #958
"""


from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return None

        queue = deque([root])
        isNull = False

        while queue:
            curr = queue.popleft()

            if not curr:
                isNull = True
                continue

            if isNull:
                return False

            queue.append(curr.left)
            queue.append(curr.right)

        return True



if __name__ == "__main__":

    solution = Solution()

    def buildTree(nodes, root, i=0):
        if i >= len(nodes):
            return None

        root = TreeNode(nodes[i])

        root.left = buildTree(nodes, root.left, 2*i+1)
        root.right = buildTree(nodes, root.right, 2*i+2)

        return root

    root = buildTree([1,2,3,4,5,6], None)
    assert solution.isCompleteTree(root) == True

    root = buildTree([1,2,3,4,5,None,7], None)
    assert solution.isCompleteTree(root) == False
