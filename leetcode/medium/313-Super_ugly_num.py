"""
    Leetcode #313
"""


from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        if not n or n == 0 or n == 1:
            return n

        res = [0] * n
        res[0] = 1

        # tracker multication for each prime
        # after each iteration
        # like 2 for 2, 1 for 7, 1 for 13, 1 for 19
        tracker = [0] * len(primes)

        for i in range(1, n):
            res[i] = float("inf")
            for j in range(len(primes)):
                if primes[j] * res[tracker[j]] == res[i-1]:
                    tracker[j] += 1

                res[i] = min(res[i], primes[j] * res[tracker[j]])

        return res[n-1]


if __name__ == "__main__":

    assert Solution().nthSuperUglyNumber(12, [2,7,13,19]) == 32
