"""
    Leetcode #693
"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = bin(n)
        return all(bits[i] != bits[i+1] for i in range(len(bits)-1))

    def hasAlternatingBits_ALT(self, n: int) -> bool:
        n, cur = divmod(n, 2)
        while n:
            if cur == n % 2: return False
            n, cur = divmod(n, 2)
        return True


if __name__ == "__main__":

    solution = Solution()

    assert solution.hasAlternatingBits(5) == True
    assert solution.hasAlternatingBits(7) == False
    assert solution.hasAlternatingBits(11) == False

    assert solution.hasAlternatingBits_ALT(5) == True
    assert solution.hasAlternatingBits_ALT(7) == False
    assert solution.hasAlternatingBits_ALT(11) == False

