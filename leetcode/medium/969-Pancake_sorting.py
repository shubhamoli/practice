"""
    Leetcode
"""


from leetcode.utils import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        N = len(A)

        res = []
        while N > 1:
            max_idx = -1
            _max = float("-inf")

            # find largest element till this length
            for i in range(N):
                if A[i] > _max:
                    _max = A[i]
                    max_idx = i

            # reverse 0 --- max_idx
            # to take largest element to first
            res.append(max_idx+1)
            A = A[:max_idx+1][::-1] + A[max_idx+1:]

            # Again reverse this array to take largest element to last
            res.append(N)
            A = A[:N][::-1] + A[N:]

            N -= 1

        return res


    def pancakeSort_ALT(self, A: List[int]) -> List[int]:

        res = []

        for x in range(len(A), 1, -1):
            # here max num will be x
            # because we are iterating from right end
            i = A.index(x)

            res.extend([i + 1, x])

            A = A[:i:-1] + A[:i]

        return res




if __name__ == "__main__":

    solution = Solution()

    assert solution.pancakeSort([3,2,4,1]) == [3, 4, 2, 3, 1, 2]
    assert solution.pancakeSort_ALT([1,2,3]) == [3, 3, 2, 2]


