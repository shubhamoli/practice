"""
    Leetcode #306
"""


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        length = len(num)
        # first find two numbers
        # then check them for third
        for i in range(1, length):
            for j in range(i + 1, length):
                first, second, remaining = num[:i], num[i:j], num[j:]
                if (first.startswith('0') and first != '0') or (second.startswith('0') and second != '0'):
                    continue
                while remaining:
                    third = str(int(first) + int(second))
                    if not remaining.startswith(third):
                        break
                    first = second
                    second = third
                    remaining = remaining[len(third):]
                if not remaining:
                    return True

        return False


if __name__ == "__main__":

    assert Solution().isAdditiveNumber("112358") == True
    assert Solution().isAdditiveNumber("199100199") == True

