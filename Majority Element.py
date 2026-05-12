class Solution:
    def majorityElement(self, nums):
        count = 0      # biến đếm
        candidate = 0  # ứng viên majority

        for num in nums:
            if count == 0:
                candidate = num  # chọn ứng viên mới

            if num == candidate:
                count += 1       # cùng ứng viên → tăng
            else:
                count -= 1       # khác → giảm

        return candidate  # phần tử xuất hiện > n/2