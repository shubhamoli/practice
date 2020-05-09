"""
    Leetcode #137
"""


from typing import List
from collections import Counter


class Solution:
    # linear but extra memory
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return None

        # O(n) operation
        store = Counter(nums)

        for i in nums:
            if store[i] == 1:
                return i

        return None

    def singleNumber_NO_SPACE(self, nums: List[int]) -> int:
        if not nums:
            return None

        ones = 0;
        twos = 0;

        for i in nums:
            ones = (~twos) & (ones ^ i)
            twos = (~ones) & (twos ^ i)

        return ones


if __name__ == "__main__":

    solution = Solution()

    assert solution.singleNumber([2,2,3,2]) == 3
    assert solution.singleNumber([0,1,0,1,0,1,99]) == 99

    assert solution.singleNumber_NO_SPACE([2,2,3,2]) == 3
    assert solution.singleNumber_NO_SPACE([0,1,0,1,0,1,99]) == 99
