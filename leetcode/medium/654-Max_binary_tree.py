"""
    Leetcode #654
"""


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(n^2)
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        def helper(nums, l, r):
            if l == r:
                return

            _max = float("-inf")
            _idx = 0    # track index of max value
            for i in range(l, r):
                if nums[i] > _max:
                    _max = nums[i]
                    _idx = i

            root = TreeNode(nums[_idx])

            root.left = helper(nums, l, _idx)
            root.right = helper(nums, _idx+1, r)

            return root


        return helper(nums, 0, len(nums))




if __name__ == "__main__":

    solution = Solution()

    res = []
    def inorderTraverse(root):
        if not root:
            return

        inorderTraverse(root.left)
        res.append(root.val)
        inorderTraverse(root.right)

        return res

    # since inorder traversal of generated will return original array
    nums = [3,2,1,6,0,5]
    assert inorderTraverse(solution.constructMaximumBinaryTree([3,2,1,6,0,5])) == nums
