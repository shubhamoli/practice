"""
    Leetcode #56
"""


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # to pass few test cases
        # we hvae to sort
        intervals.sort()  # default by 0th index
        merged = []

        for i in range(len(intervals)):
            if merged == []:
                merged.append(intervals[i])
            else:
                previous_end = merged[-1][1]
                current_start = intervals[i][0]
                current_end = intervals[i][1]
                if previous_end >= current_start: # overlap
                    merged[-1][1] = max(previous_end, current_end)
                else:
                    merged.append(intervals[i])

        return merged


if __name__ == "__main__":

    solution = Solution()

    print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))     # [[1,6],[8,10],[15,18]]
    print(solution.merge([[1,4],[4,5]]))     # [[1,5]]
