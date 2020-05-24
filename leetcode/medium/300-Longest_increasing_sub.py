"""
    Leetcode #300
"""


from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        inc = [float("inf")] * len(nums)

        size = 0
        for num in nums:
            i = bisect.bisect_left(inc, num)
            inc[i] = num
            size = max(i+1, size)

        return size

if __name__ == "__main__":

    assert Solution().lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
