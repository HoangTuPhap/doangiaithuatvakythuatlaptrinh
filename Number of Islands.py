class Solution:
    def numIslands(self, grid):
        # DFS flood fill: mỗi lần gặp '1' chưa thăm → tăng count và "xóa" đảo đó

        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        count = 0

        def dfs(i, j):
            # Nếu ra ngoài biên hoặc gặp nước → dừng
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == '0':
                return

            # Đánh dấu đã thăm bằng cách đổi thành '0'
            grid[i][j] = '0'

            # Lan sang 4 hướng
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Duyệt toàn bộ grid
        for i in range(row):
            for j in range(col):

                # Nếu gặp đất → có đảo mới
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)  # xóa toàn bộ đảo đó

        return count