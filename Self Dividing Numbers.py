class Solution:
    def selfDividingNumbers(self, left, right):
        res = []

        for num in range(left, right + 1):
            x = num
            ok = True

            while x > 0:
                digit = x % 10

                if digit == 0 or num % digit != 0:
                    ok = False
                    break

                x //= 10

            if ok:
                res.append(num)

        return res