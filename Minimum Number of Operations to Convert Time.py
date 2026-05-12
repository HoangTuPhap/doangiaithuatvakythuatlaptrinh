class Solution:
    def convertTime(self, current, correct):
        h1, m1 = map(int, current.split(":"))
        h2, m2 = map(int, correct.split(":"))

        current_minutes = h1 * 60 + m1
        correct_minutes = h2 * 60 + m2

        diff = correct_minutes - current_minutes
        ops = 0

        for x in [60, 15, 5, 1]:
            ops += diff // x
            diff %= x

        return ops  