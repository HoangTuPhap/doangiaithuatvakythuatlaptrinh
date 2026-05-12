class Solution:
    def canAliceWin(self, n):
        need = 10
        turn = 0
        while n >= need:
            n -= need
            need -= 1
            turn += 1
        return turn % 2 == 1