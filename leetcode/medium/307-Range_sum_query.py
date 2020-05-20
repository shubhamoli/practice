"""
    Leetcode #307
"""


from typing import List


#Segment tree node
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

# using segment tree as array is going to be chagned frequently
# so updating using segment is O(logn)
# for DP it will be O(n)
class NumArray:

    def __init__(self, nums: List[int]):
        self.root = self._createTree(nums, 0, len(nums)-1)

    def _createTree(self, nums, l, r):
        if l > r:
            return None

        # leaf node
        if l == r:
            n = Node(l, r)
            n.total = nums[l]
            return n

        mid = (l + r) // 2

        root = Node(l, r)

        root.left = self._createTree(nums, l, mid)
        root.right = self._createTree(nums, mid+1, r)

        root.total = root.left.total + root.right.total

        return root

    def update(self, i: int, val: int) -> None:

        def helper(root, i, val):
            if root.start == root.end:
                root.total = val
                return val

            mid = (root.start + root.end) // 2

            if i <= mid:
                helper(root.left, i, val)
            else:
                helper(root.right, i, val)

            root.total = root.left.total + root.right.total

        helper(self.root, i, val)

    def sumRange(self, i: int, j: int) -> int:
        def helper(root, i, j):

            if root.start == i and root.end == j:
                return root.total

            mid = (root.start + root.end) // 2

            if j <= mid:
               return helper(root.left, i, j)

            elif i >= mid + 1:
               return helper(root.right, i, j)

            else:
               return helper(root.left, i, mid) + helper(root.right, mid+1, j)


        return helper(self.root, i, j)


# for immutable array
class NumArray_DP:

    def __init__(self, nums):
        self.dp = [0] * (len(nums)+1)
        self.dp[0] = 0

        for i in range(1, len(nums)+1):
            # dp[i] will save sum upto i-1 and nums[i-1]
            self.dp[i] = self.dp[i-1] + nums[i-1]

    def sumRange(self, i, j):
        return self.dp[j+1] - self.dp[i]


if __name__ == "__main__":

    obj = NumArray([1, 3, 5])

    assert obj.sumRange(0, 2) == 9
    obj.update(1, 2)
    assert obj.sumRange(0, 2) == 8

    obj = NumArray_DP([1, 3, 5])
    assert obj.sumRange(0, 2) == 9
