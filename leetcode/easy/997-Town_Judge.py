"""
    Leetcode #997
"""


from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and trust == []:
            return N

        if not trust:
            return -1

        if N < 2:
            return -1

        tracker = defaultdict(list)

        for i in range(0, N):
            tracker[i+1] = []

        for a, b in trust:
            tracker[a].append(b)

        # check for first property
        # The town judge trusts nobody.
        found = -1
        for i, count in tracker.items():
            if count == []:
                found = i

        if found == -1:
            return -1

        # check for second property
        # Eerybody (except for the town judge) trusts the town judge.
        for i, count in tracker.items():
            if i != found and not (found in count):
                return -1

        return found

    
    def findJudge_OPTI(self, N: int, trust: List[List[int]]) -> int:
        trusted = [0] * (N+1)

        # if a trust b
        # decrement a's counter
        # and increment b's counter
        for a, b in trust:
            trusted[a] -= 1
            trusted[b] += 1

        # only judge will have counter == N-1
        for i in range(1, N+1):
            if trusted[i] == N-1:
                return i

        return -1


if __name__ == "__main__":

    solution = Solution()

    assert solution.findJudge(2, [[1,2]]) == 2
    assert solution.findJudge(3, [[1,3],[2,3]]) == 3
    assert solution.findJudge(3, [[1,3],[2,3],[3,1]]) == -1
    assert solution.findJudge(3, [[1,2],[2,3]]) == -1
    assert solution.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]) == 3

    assert solution.findJudge_OPTI(2, [[1,2]]) == 2
    assert solution.findJudge_OPTI(3, [[1,3],[2,3]]) == 3
    assert solution.findJudge_OPTI(3, [[1,3],[2,3],[3,1]]) == -1
    assert solution.findJudge_OPTI(3, [[1,2],[2,3]]) == -1
    assert solution.findJudge_OPTI(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]) == 3

