"""
    Leetcode #34
"""


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearchLeft():
                left, right = 0, len(nums) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if target > nums[mid]: left = mid + 1
                    else: right = mid - 1
                return left

        def binarySearchRight():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if target >= nums[mid]: left = mid + 1
                else: right = mid - 1
            return right

        left, right = binarySearchLeft(), binarySearchRight()
        return [left, right] if left <= right else [-1, -1]


if __name__ == "__main__":

    solution = Solution()
    print(solution.searchRange([5,7,7,8,8,10], 8))
    # assert solution.searchRange([5,7,7,8,8,10], 8) == [3, 4]
    # assert solution.searchRange([5,7,7,8,8,10], 6) == [-1, -1]
    # assert solution.searchRange([5,7,7,8,8,8,8,8,8,10], 6) == [-1, -1]
