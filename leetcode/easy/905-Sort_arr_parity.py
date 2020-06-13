"""
    Leetcode #905
"""


from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if not A:
            return []

        even = []
        odd = []

        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        even.extend(odd)
        return even

    def sortArrayByParity_ALT(self, A: List[int]) -> List[int]:
        if not A:
            return []

        # leveraging the fact that any combination is accpeted
        l = 0
        r = len(A) - 1
        while l < r:
            if A[l] % 2 != 0:
                A[l], A[r] = A[r], A[l]
                r -= 1
            else:
                l += 1

        return A


if __name__ == "__main__":

    solution = Solution()

    assert solution.sortArrayByParity([3,1,2,4]) == [2,4,3,1]
    assert solution.sortArrayByParity_ALT([3,1,2,4]) == [4, 2, 1, 3]

