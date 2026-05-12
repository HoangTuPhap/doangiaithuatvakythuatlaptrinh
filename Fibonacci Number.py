class Solution:
    def fib(self, n):
        if n <= 1:
            return n  # F(0)=0, F(1)=1

        a, b = 0, 1  # a=F(0), b=F(1)

        for _ in range(2, n + 1):
            a, b = b, a + b  # cập nhật: a=F(i-1), b=F(i)

        return b  # F(n)