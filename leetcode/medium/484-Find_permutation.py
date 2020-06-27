"""
    Leetcode #484
"""


from leetcode.utils import List


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        if not s:
            return []

        N = len(s)

        res = [0] * (N + 1)
        _idx = 0

        stk = []
        for i in range(1, N+1):
            if s[i-1] == 'I':
                stk.append(i)
                while stk:
                    res[_idx] = stk.pop()
                    _idx += 1
            else:
                # append i in stk
                # for s[i] == 'D'
                # so that it can be reversed later
                stk.append(i)

        stk.append(N+1)
        while stk:
            res[_idx] = stk.pop()
            _idx += 1

        return res




if __name__ == "__main__":

    solution = Solution()

    assert solution.findPermutation("I") == [1, 2]
    assert solution.findPermutation("DI") == [2, 1, 3]

