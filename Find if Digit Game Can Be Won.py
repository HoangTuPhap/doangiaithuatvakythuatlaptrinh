class Solution:
    def canAliceWin(self, nums):
        sum_single = 0  # tổng các số 1 chữ số (1 → 9)
        sum_double = 0  # tổng các số 2 chữ số (10 → 99)

        for num in nums:
            if num < 10:
                sum_single += num   # cộng vào nhóm 1 chữ số
            else:
                sum_double += num   # cộng vào nhóm 2 chữ số

        total = sum_single + sum_double  # tổng tất cả phần tử

        # Nếu chọn 1 chữ số mà thắng
        if sum_single > total - sum_single:
            return True

        # Nếu chọn 2 chữ số mà thắng
        if sum_double > total - sum_double:
            return True

        return False  # không có cách nào thắng