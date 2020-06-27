"""
    Leetcode #464
"""


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        seen = {}
        def helper(choices, total):

            if choices[-1] >= total:
                return True

            # check if subproblem is already solved
            key = tuple(choices)
            if key in seen:
                return seen[key]

            for i in range(len(choices)):
                # if second player can win for ith round
                if not helper(choices[:i] + choices[i+1:], total - choices[i]):
                    # we won
                    seen[i] = True
                    return True

            # if we reach here then it means, second player won in loop above
            # so set it false
            seen[key] = False
            return False


        choices = list(range(1, maxChoosableInteger + 1))

        # sum of consecutive integers
        _sum = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2

        if _sum < desiredTotal:
            return False

        # if len is odd, means first player's turn
        if _sum == desiredTotal and len(choices) % 2:
            return True

        return helper(choices, desiredTotal)



if __name__ == "__main__":

    solution = Solution()

    assert solution.canIWin(10, 11) == False
