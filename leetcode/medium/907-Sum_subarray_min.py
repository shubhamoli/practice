"""
    Leetcode #907
"""


from typing import List

class Solution:
    def sumSubarrayMins_BF(self, A: List[int]) -> int:
        if not A:
            return 0

        _sum = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)+1):
                tmp = A[i:j]
                _sum += min(tmp)

        return _sum

    def sumSubarrayMins(self, A: List[int]) -> int:
        if not A:
            return 0

        N = len(A)
        mod = 10**9 + 7

        left = [0] * N
        right = [0] * N

        stk = []
        # IDEA:
        # res = sum(A[i] * f(i))
        # where f(i) is the number of subarrays,
        # in which A[i] is the minimum. for each ith element
        #
        # we need to find length of A[L...i] and A[i...R] where A[i] is Minimum

        # for ith number keep number of element greater the A[i] on left side
        # A[L...i]
        for i in range(N):
            count = 1
            while stk and stk[-1][0] > A[i]:
                count += stk.pop()[1]

            left[i] = count
            stk.append([A[i], count])

        # for ith number keep number of element greater the A[i] on left side
        # A[L...i]
        stk = []
        for i in range(N)[::-1]:
            count = 1
            while stk and stk[-1][0] >= A[i]:
                count += stk.pop()[1]

            right[i] = count
            stk.append([A[i], count])

        return sum(a * l * r for a, l, r in zip(A, left, right))


    def sumSubarrayMins_ALT(self, A: List[int]) -> int:
        res = 0
        s = []
        A = [0] + A + [0]
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res % (10**9 + 7)



if __name__ == "__main__":

    solution = Solution()

    assert solution.sumSubarrayMins_BF([3,1,2,4]) == 17
    assert solution.sumSubarrayMins([3,1,2,4]) == 17
    assert solution.sumSubarrayMins_ALT([3,1,2,4]) == 17



