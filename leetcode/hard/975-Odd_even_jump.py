"""
    Leetcode #975
"""


from typing import List

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        if not A:
            return 0

        N = len(A)

        next_higher = [0] * N
        next_lower = [0] * N

        stk = []
        # for odd jumps
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stk and stk[-1] < i:
                next_higher[stk.pop()] = i

            stk.append(i)

        # for even jumps
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stk and stk[-1] < i:
                next_lower[stk.pop()] = i

            stk.append(i)

        high = [0] * N
        low = [0] * N
        high[-1] = 1    # can't jump further
        low[-1] = 1    # can't jump further

        for i in range(N-1)[::-1]:
            high[i] = low[next_higher[i]]
            low[i] = high[next_lower[i]]

        return sum(high)



if __name__ == "__main__":

    solution = Solution()

    assert solution.oddEvenJumps([10,13,12,14,15]) == 2

