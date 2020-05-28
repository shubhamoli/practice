"""
    Leetcode #380
"""


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._nums = []
        self._tracker = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if self._tracker.get(val) is not None:
            return False

        self._nums.append(val)
        self._tracker[val] = len(self._nums) - 1
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if self._tracker.get(val) is None:
            return False

        idx, last = self._tracker[val], self._nums[-1]
        self._nums[idx], self._tracker[last] = last, idx
        self._nums.pop()
        self._tracker.pop(val, 0)

        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self._nums[random.randint(0, len(self._nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
