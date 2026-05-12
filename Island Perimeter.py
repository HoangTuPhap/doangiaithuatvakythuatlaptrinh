class Solution:
    def islandPerimeter(self, grid):
        # Không dùng type hint vì môi trường có thể là Python < 3.9

        row = len(grid)
        col = len(grid[0])
        perimeter = 0

        # Duyệt từng ô
        for i in range(row):
            for j in range(col):

                # Nếu là đất
                if grid[i][j] == 1:

                    # Mỗi ô đất có 4 cạnh
                    perimeter += 4

                    # Nếu phía trên là đất → trừ 2 cạnh chung
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2

                    # Nếu bên trái là đất → trừ 2 cạnh chung
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter