"""
    Leetcode #1403
"""


from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort(reverse=True)

        res = []
        _sum = sum(nums)
        _curr_sum = 0

        for i in nums:
            _curr_sum += i
            _sum -= i
            res.append(i)
            if _curr_sum > _sum:
                break

        return res


if __name__ == "__main__":

    solution = Solution()

    assert solution.minSubsequence([4,3,10,9,8]) == [10, 9]
    assert solution.minSubsequence([4,4,7,6,7]) == [7, 7, 6]

