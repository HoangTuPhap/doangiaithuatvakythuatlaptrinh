class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x):
        digit_sum = sum(int(d) for d in str(x))

        if x % digit_sum == 0:
            return digit_sum

        return -1