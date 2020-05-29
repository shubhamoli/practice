"""
    Leetcode !442
"""


from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        d = {0:[-1]} #helps in implementation

        res = 0 # running xor value
        count = 0

        for i in range(len(arr)):
            res = res ^ arr[i]
            if res in d: # Point 2 above, if we find the vaue already in dict
                temp = [i-x-1 for x in d[res]] #find all j, and add
                count += sum(temp)
                d[res].append(i)
            else:
                d[res] = [i]#save in dict if not already present Point 1 above

        return count


if __name__ == "__main__":

    solution = Solution()

    assert solution.countTriplets([2,3,1,6,7]) == 4
