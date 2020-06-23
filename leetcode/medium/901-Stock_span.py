"""
    Leetcode #901
"""


class StockSpanner:

    def __init__(self):
        self.stocks = []

    # O(n^2) operation
    # for each insertion, we have to check left to its element
    # which in worst can be O(n) itself
    def next(self, price: int) -> int:
        self.stocks.append(price)
        return self.span(len(self.stocks))

    def span(self, idx):
        count = 0
        curr = self.stocks[idx-1]
        while idx > 0:
            if self.stocks[idx-1] <= curr:
                count += 1
            if self.stocks[idx-1] > curr:
                break
            idx -= 1

        return count

    # using monotonic stacks
    # it may seem more than O(n) in first sight
    # but since each element is inserted and popped from stack only once
    # so it O(2n) == O(n) operation only
    def next_OPTI(self, idx):
        while self.stk and self.stocks[self.stk[-1]] <= price:
            self.stk.pop()

        self.stocks.append(price)
        self.stk.append(len(self.stocks)-1)

        return self.stk[-1] - self.stk[-2] if len(self.stk) >  1 else self.stk[-1] + 1


if __name__ == "__main__":

    s = StockSpanner()

    assert s.next(100) == 1
    assert s.next(80) == 1
    assert s.next(60) == 1
    assert s.next(70) == 2
    assert s.next(60) == 1
    assert s.next(75) == 4
    assert s.next(85) == 6

