"""
    Leetcode #454
"""


from typing import List
from collections import Counter


class Solution:
    # O(N^3)
    def fourSumCount_BRUTE(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if len(A) == len(B) == len(C) == len(D) == 0:
            return

        D_set = set(D)

        count = 0
        for i in A:
            for j in B:
                for k in C:
                    if -(i+j+k) in D_set:
                        count += 1

        return count

    # O(N^2)
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count = 0

        store = {}
        for a in A:
            for b in B:
                store[a+b] = store.get(a+b, 0) + 1

        for c in C:
            for d in D:
                if -(c+d) in store:
                    count += store.get(-(c+d))

        return count

    # this is faster and fancier than above
    def fourSumCount_ALT(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count = 0

        store = Counter([a+b for a in A for b in B])
        return sum(store[-(c+d)] for c in C for d in D)



if __name__ == "__main__":

    solution = Solution()

    assert solution.fourSumCount_BRUTE([ 1, 2 ], [-2,-1], [-1, 2],  [0, 2]) == 2
    assert solution.fourSumCount([ 1, 2 ], [-2,-1], [-1, 2],  [0, 2]) == 2
    assert solution.fourSumCount_ALT([ 1, 2 ], [-2,-1], [-1, 2],  [0, 2]) == 2
