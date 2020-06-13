"""
    Leetcode #401
"""


from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        return  ["%d:%02d" % (h, m) 
                    for h in range(12) for m in range(60)
                    if (bin(h)+bin(m)).count("1") == num]



if __name__ == "__main__":

    solution = Solution()

    print(solution.readBinaryWatch(1))  # ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
