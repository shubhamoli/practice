"""
    Leetcode #229
"""


from typing import List
from collections import Counter

class Solution:

    # O(n) both time and space
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        store = Counter(nums)

        res = []
        for i in store.keys():
            if store[i] > (len(nums)) // 3:
                res.append(i)

        return res


    # O(n) in time and O(1) in space
    # Boyer-Moore Majority Vote algo
    def majorityElement_OPTI(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        count1, count2, candidate1, candidate2 = 0, 0, 0, 1

        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1

        res = [n for n in (candidate1, candidate2)
                        if nums.count(n) > len(nums) // 3]

        print(res)
        return res


if __name__ == "__main__":

    solution = Solution()

    assert solution.majorityElement([3,2,3]) == [3]
    assert solution.majorityElement([1,1,1,3,3,2,2,2]) == [1, 2]

    assert solution.majorityElement_OPTI([3,2,3]) == [3]
    assert solution.majorityElement_OPTI([1,1,1,3,3,2,2,2]) == [1, 2]

