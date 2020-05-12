"""
    Leetcode #152
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = _min = _max = nums[0]

        for i in range(1, len(nums)):
            # if current is -ve integer then
            # current max will become new min
            # and new min will become current max
            if nums[i] < 0:
                _min, _max = _max, _min

            _max = max(nums[i], _max*nums[i])
            _min = min(nums[i], _min*nums[i])


            res = max(_max, res)

        return res


if __name__ == "__main__":

    solution = Solution()

    assert solution.maxProduct([2,3,-2,4]) == 6
    assert solution.maxProduct([-2,0,-1]) == 0
