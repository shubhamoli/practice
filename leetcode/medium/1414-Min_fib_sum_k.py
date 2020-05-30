"""
    Leetcode #1414
"""

class Solution:
    # It is guaranteed that for the given constraints
    # we can always find such fibonacci numbers that sum k.
    def findMinFibonacciNumbers(self, k: int) -> int:
        #find fib numbers up to k
        fibo = [1,1]
        while fibo[-1] <= k:
            fibo.append(fibo[-1] + fibo[-2])

        print(fibo)
        # here we have our inventory
        # greedy approach
        value = 0
        count = 0
        while k > 0:
            for i in fibo:
                if i <= k:
                    value = i
            count += 1
            k -= value

        return count





if __name__ == "__main__":

    solution = Solution()

    # assert solution.findMinFibonacciNumbers(7) == 2
    # assert solution.findMinFibonacciNumbers(10) == 2
    assert solution.findMinFibonacciNumbers(19) == 3
