"""
    Leetcode #456
"""


from typing import List

class Solution:
    # O(N^3)
    def find132pattern_BF(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if i < j < k and nums[i] < nums[k] < nums[j]:
                        return True

        return False

    # O(N^2)
    # keep _min fixed instead of looping
    def find132pattern_BF_OPTI(self, nums: List[int]) -> bool:
        _min = float("inf")
        for j in range(len(nums)):
            _min = min(_min, nums[j])
            if _min == nums[j]:
                continue

            for k in range(len(nums)-1, j-1, -1):
                if _min < nums[k] < nums[j]:
                    return True

        return False



    # O(N)
    def find132pattern_OPTI(self, nums: List[int]) -> bool:
        third = float("-inf")

        stk = []
        for num in reversed(nums):
            if num < third:
                return True

            while stk and stk[-1] < num:
                third = stk.pop()

            stk.append(num)

        return False




if __name__ == "__main__":

    solution = Solution()

    assert solution.find132pattern_BF([1, 2, 3, 4]) == False
    assert solution.find132pattern_BF([3, 1, 4, 2]) == True
    assert solution.find132pattern_BF([-1, 3, 2, 0]) == True

    assert solution.find132pattern_BF_OPTI([1, 2, 3, 4]) == False
    assert solution.find132pattern_BF_OPTI([3, 1, 4, 2]) == True
    assert solution.find132pattern_BF_OPTI([-1, 3, 2, 0]) == True

    assert solution.find132pattern_OPTI([1, 2, 3, 4]) == False
    assert solution.find132pattern_OPTI([3, 1, 4, 2]) == True
    assert solution.find132pattern_OPTI([-1, 3, 2, 0]) == True
    assert solution.find132pattern_OPTI([3,5,0,3,4]) == True
