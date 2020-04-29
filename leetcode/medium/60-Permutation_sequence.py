"""
    Leetcode #60
"""

class Solution:
    count = 0
    perm = None
    def getPermutation(self, n: int, k: int) -> str:

        nums = [i for i in range(1, n+1)]

        res = []
        store = {}

        def helper(nums, curr):

            if len(curr) == len(nums):
                self.count = self.count + 1
                if self.count == k:
                    self.perm = curr[:]
                    return True
                return

            for i in nums:
                if store.get(i):
                    continue
                curr.append(i)
                store[i] = True

                if (helper(nums, curr)): return

                store[i] = False
                curr.pop()


        helper(nums, [])
        return "".join(map(str, self.perm))

    def getPermutation_OPTI(self, n: int, k: int) -> str:

        nums = [i for i in range(1, n+1)]
        res = ""

        k -= 1
        while n:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            res += str(nums.pop(index))

        return res

if __name__ == "__main__":

    solution = Solution()

    print(solution.getPermutation(3, 3))
