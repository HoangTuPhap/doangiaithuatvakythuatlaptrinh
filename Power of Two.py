class Solution:
    def isPowerOfTwo(self, n):
        # n phải > 0
        # số là lũy thừa của 2 khi chỉ có đúng 1 bit = 1
        # n & (n - 1) == 0 sẽ loại bỏ bit 1 đó → còn 0

        return n > 0 and (n & (n - 1)) == 0