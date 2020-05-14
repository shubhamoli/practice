"""
    Leetcode #179
"""


from typing import List
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""

        if len(nums) == 1:
            return str(nums[0])

        # convert nums to str for lexographical comparison
        nums_str = [str(i) for i in nums]

        nums_str = sorted(nums_str, key=functools.cmp_to_key(self.cmp_func))

        return ''.join(nums_str).lstrip('0') or "0"

    def cmp_func(self, x, y):
        if x + y > y + x:
            return -1
        return 1

if __name__ == "__main__":

    solution = Solution()

    assert solution.largestNumber([10,2]) == "210"
    assert solution.largestNumber([3,30,34,5,9]) == "9534330"

