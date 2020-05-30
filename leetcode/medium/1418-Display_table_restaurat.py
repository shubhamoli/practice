"""
    Leetcode #1418
"""


from typing import List
from collections import defaultdict, Counter

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        store = defaultdict(Counter)

        # count distinct meals
        # required for table header
        meals = set()
        for name, table, item in orders:
            store[table][item] += 1
            meals.add(item)

        # create table header
        meals = sorted(meals)
        res = [['Table'] + [item for item in meals]]

        for table in sorted(store, key=int):
            res.append([table] + [str(store[table][item]) for item in meals])

        return res


if __name__ == "__main__":

    solution = Solution()

    print(solution.displayTable([  ["David","3","Ceviche"],
                                   ["Corina","10","Beef Burrito"],
                                   ["David","3","Fried Chicken"],
                                   ["Carla","5","Water"],
                                   ["Carla","5","Ceviche"],
                                   ["Rous","3","Ceviche"]]))
