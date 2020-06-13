"""
    Leetcode #982
"""


from typing import List
from collections import defaultdict

class Solution:
    def countTriplets(self, A: List[int]) -> int:
        store = defaultdict(int)

        for i in range(len(A)):
            for j in range(len(A)):
                store[A[i] & A[j]] += 1

        ans = 0
        for i in range(len(A)):
            for key in store.keys():
                if key & A[i] == 0:
                    ans += store[key]

        return ans


if __name__ == "__main__":

    solution = Solution()

    assert solution.countTriplets([2, 1, 3]) == 12
