"""
    Leetcode #989
"""

from leetcode.utils import List

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        if not A:
            return list(k)

        if not K:
            return A

        for i in reversed(range(len(A))):
            # 1 2 0 0
            #     3 4
            K, d = divmod(K, 10)
            carry, A[i] = divmod(A[i] + d, 10)

            K += carry
            if not K:
                break

        if K:
            A = list(map(int, str(K))) + A

        return A

    def addToArrayForm_ALT(self, A: List[int], K: int) -> List[int]:
        res = []
        i = len(A) - 1

        while K > 0 or i >= 0:
            K, rmd = divmod(K + (A[i] if i >= 0 else 0), 10)
            res.append(rmd)
            i -= 1

        return list(reversed(res))


if __name__ == "__main__":

    solution = Solution()

    assert solution.addToArrayForm([1, 2, 0, 0], 34) == [1, 2, 3, 4]
    assert solution.addToArrayForm([2, 1, 5], 806) == [1, 0, 2, 1]
    assert solution.addToArrayForm([9,9,9,9,9,9,9,9,9,9], 1) == [1,0,0,0,0,0,0,0,0,0,0]
    assert solution.addToArrayForm_ALT([9,9,9,9,9,9,9,9,9,9], 1) == [1,0,0,0,0,0,0,0,0,0,0]

