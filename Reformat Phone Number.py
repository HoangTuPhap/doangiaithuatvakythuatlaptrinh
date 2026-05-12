class Solution:
    def reformatNumber(self, number):
        digits = ""

        for ch in number:
            if ch.isdigit():
                digits += ch

        res = []
        i = 0
        n = len(digits)

        while n - i > 4:
            res.append(digits[i:i+3])
            i += 3

        if n - i == 4:
            res.append(digits[i:i+2])
            res.append(digits[i+2:i+4])
        else:
            res.append(digits[i:])

        return "-".join(res)