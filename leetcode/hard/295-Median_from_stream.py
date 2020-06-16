"""
    Leetcode #295
"""


import bisect

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._nums = []

    # addNum: O(1)
    # findMedian: O(nlogn)
    def addNum(self, num: int) -> None:
        self._nums.append(num)

    # to keep nusm sorted every time
    # we will search for suitable index (binary search)
    # and insert num at correct place so that nums will always be sorted
    #
    # addNum: O(logn)
    # findMedian: O(1)
    def addNum_2(self, num: int) -> None:
        bisect.insort(self._nums, num)

    def findMedian(self) -> float:
        # self._nums.sort()
        N = len(self._nums)
        if N % 2 == 1:
            return self._nums[N//2]
        else:
            return (self._nums[N//2] + self._nums[N//2-1]) / 2


if __name__ == "__main__":

    # Your MedianFinder object will be instantiated and called as such:
    obj = MedianFinder()

    # obj.addNum(1)
    # obj.addNum(1)
    obj.addNum_2(1)
    obj.addNum_2(2)

    assert obj.findMedian() == 1.5

    obj.addNum_2(3)

    assert obj.findMedian() == 2



