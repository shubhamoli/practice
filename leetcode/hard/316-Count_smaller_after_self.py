"""
    Leetcode #316
"""

from typing import List

class Solution:
    # O(N^2)
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        res = [0] * len(nums)

        for i in range(len(nums)):
            tmp = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] < tmp:
                    res[i] += 1

        return res

    # O(nlogn) - using same logic as mergesort
    # because elements while sorting which are smaller in right are transferred to left
    def countSmaller_OPTI(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        def divide(tupn):
            if len(tupn) == 1:
                return tupn

            mid = len(tupn) // 2

            left = divide(tupn[:mid])
            right = divide(tupn[mid:])

            return conquer(left, right)

        def conquer(left, right):
            sor = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:
                    sor.append(left[i])
                    # tracking smaller on right
                    res[left[i][1]] += len(right) - j
                    i += 1
                else:
                    sor.append(right[j])
                    j += 1

            sor.extend(left[i:] or right[j:])
            return sor

        res = [0] * len(nums)
        tupn = [(n, i) for i, n in enumerate(nums)]
        divide(tupn)

        return res


if __name__ == "__main__":

    solution = Solution()

    assert solution.countSmaller([5,2,6,1]) == [2,1,1,0]
    assert solution.countSmaller_OPTI([5,2,6,1]) == [2,1,1,0]

