"""
    Leetcode #368
"""

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        res = []
        mem = [-1] * len(nums)
        def helper(idx, curr, prev):
            nonlocal res
            if len(curr) > len(res):
                res = curr[:]

            for i in range(idx, len(nums)):
                # prune: for the current value, if it has been visited with a larger
                # set, then skip it
                if len(curr) > mem[i] and nums[i] % prev == 0:
                    mem[i] = len(curr)
                    curr.append(nums[i])
                    helper(i+1, curr, nums[i])
                    curr.pop()

        nums.sort()
        helper(0, [], 1)

        return res


if __name__ == "__main__":

    solution = Solution()

    assert solution.largestDivisibleSubset([1,2,3]) == [1,2]
    assert solution.largestDivisibleSubset([1,2,4,8]) == [1,2,4,8]
