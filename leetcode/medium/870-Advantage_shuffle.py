"""
    Leetcode #870
"""


from typing import List
from collections import defaultdict

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        a = sorted(A)
        b = sorted(B)

        store = defaultdict(list)
        remaining = []
        j = 0

        for i in range(len(a)):
            if a[i] > b[j]:
                store[b[j]].append(a[i])
                j += 1
            else:
                remaining.append(a[i])

        return [store[n].pop() if n in store and len(store[n]) > 0 else remaining.pop() for n in B]


if __name__ == "__main__":

    solution = Solution()

    assert solution.advantageCount([2,7,11,15], [1,10,4,11]) == [2,11,7,15]
    assert solution.advantageCount([12,24,8,32], [13,25,32,11]) == [24,32,8,12]

