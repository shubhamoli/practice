"""
    Leetcode #90
"""


from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        def helper(curr, idx):
            res.append(curr[:])

            if idx == len(nums):
                return

            for i in range(idx, len(nums)):
                if i > 0 and idx != i and nums[i-1] == nums[i]: continue

                curr.append(nums[i])
                helper(curr, i+1)
                curr.pop()

        # sort to set duplicates together
        nums.sort()
        helper([], 0)

        return res


if __name__ == "__main__":

    print(Solution().subsetsWithDup([1,2,2]))
