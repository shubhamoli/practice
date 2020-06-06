"""
    Leetcode #1305
"""


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def inorder(root, tmp):
            if not root:
                return []

            inorder(root.left, tmp)
            tmp.append(root.val)
            inorder(root.right, tmp)

            return tmp

        in1 = inorder(root1, [])
        in2 = inorder(root2, [])

        res = []
        i = j = 0
        while i < len(in1) and j < len(in2):
            if in1[i] <= in2[j]:
                res.append(in1[i])
                i += 1
            else:
                res.append(in2[j])
                j += 1

        res.extend(in1[i:] or in2[j:])
        return res


if __name__ == "__main__":

    solution = Solution()

    def buildTree(nodes: List[int], root, i: int = 0) -> TreeNode:
        if i >= len(nodes):
            return None

        root = TreeNode(nodes[i])
        root.left = buildTree(nodes, root.left, 2*i+1)
        root.right = buildTree(nodes, root.right, 2*i+2)

        return root

    root1 = buildTree([2, 1, 4], None)
    root2 = buildTree([1, 0, 3], None)

    assert solution.getAllElements(root1, root2) == [0,1,1,2,3,4]


