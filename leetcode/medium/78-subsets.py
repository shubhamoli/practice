"""
    Leetcode #78
"""


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        if len(nums) == 1:
            return [[], nums]

        res = []

        def helper(nums, curr, idx):
            res.append(curr[:])

            if idx == len(nums):
                return

            for i in range(idx, len(nums)):
                curr.append(nums[i])
                helper(nums, curr, i+1)
                curr.pop()

        helper(nums, [], 0)
        return res


if __name__ == "__main__":

    solution = Solution()

    print(solution.subsets([1, 2, 3]))
