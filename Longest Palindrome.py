class Solution:
    def longestPalindrome(self, s):
        count = {}
        
        for c in s:
            count[c] = count.get(c, 0) + 1

        length = 0
        odd = False

        for v in count.values():
            if v % 2 == 0:
                length += v
            else:
                length += v - 1
                odd = True

        if odd:
            length += 1

        return length