class Solution:
    def passThePillow(self, n, time):
        pos = 1
        direction = 1

        for i in range(time):
            pos += direction

            if pos == n or pos == 1:
                direction *= -1

        return pos