"""
    Leetcode #11
"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Although in question
        # len(height) >= 2 always
        if not height or (len(height) < 2):
            return None

        l = 0
        r = len(height) - 1

        area = min(height[l], height[r]) * (r - l)

        while l < r:

            area = max(area, min(height[l], height[r]) * (r-l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area


if __name__ == "__main__":

    solution = Solution()

    assert solution.maxArea([]) == None
    assert solution.maxArea([1]) == None
    assert solution.maxArea([1, 1]) == 1
    assert solution.maxArea([1, 3]) == 1
    assert solution.maxArea([2, 1, 3]) == 4
    assert solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49


