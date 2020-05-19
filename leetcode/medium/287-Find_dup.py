"""
    Leetcode #287
"""


from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums)-1

        # O(nlogn)
        while low < high:
            mid = low+(high-low) // 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count <= mid:
                low = mid+1
            else:
                high = mid

        print(low)
        return low


if __name__ == "__main__":

    solution = Solution()

    assert solution.findDuplicate([1,3,4,2,2]) == 2
    assert solution.findDuplicate([3,1,3,4,2]) == 3
    assert solution.findDuplicate([1,3,3,3,4]) == 3

