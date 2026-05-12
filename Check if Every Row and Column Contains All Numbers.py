class Solution:
    def checkValid(self, matrix):
        n = len(matrix)
        required = set(range(1, n + 1))

        for row in matrix:
            if set(row) != required:
                return False

        for col in range(n):
            column = []

            for row in range(n):
                column.append(matrix[row][col])

            if set(column) != required:
                return False

        return True