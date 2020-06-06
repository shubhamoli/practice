"""
    Leetcode #1185
"""


class Solution:
    # if we know that 1/1/1971 was Friday
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        isLeapYear = lambda x: 1 if x % 400 == 0 or (x % 4 == 0 and x % 100 != 0) else 0
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        numDays = -1  # start from 1971-01-01, remove that day
        for i in range(1971, year):
            numDays += 365 + isLeapYear(i)

        numDays += sum(months[:month-1]) + day + isLeapYear(year)

        # Adding 5 because 1/1/1971 was Friday
        return days[(5+numDays)%7]


    # without knowing 1/1/1971 was friday
    # but we know what today is
    def dayOfTheWeek_2(self, day: int, month: int, year: int) -> str:
        # today of 6th june day is saturday
        # so starting days from Saturday
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def isLeapYear(year):
            return 1 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 0

        def getDay(day, month, year):
            numDays = 0
            # get num days till last year
            for y in range(year-1, 1970, -1):
                numDays += 365 + isLeapYear(y)

            numDays += sum(months[:month-1])
            numDays += day

            if month > 2:
                numDays += isLeapYear(year)

            return numDays

        k = getDay(6, 6, 2020) # today is saturday
        d = getDay(day, month, year)

        return days[(d-k)%7]



if __name__ == "__main__":

    solution = Solution()

    assert solution.dayOfTheWeek(31, 8, 2019) == "Saturday"
    assert solution.dayOfTheWeek(18, 7, 1999) == "Sunday"

    assert solution.dayOfTheWeek_2(31, 8, 2019) == "Saturday"
    assert solution.dayOfTheWeek_2(18, 7, 1999) == "Sunday"

