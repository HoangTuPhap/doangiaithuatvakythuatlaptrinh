class Solution:
    def sumOfMultiples(self, n):
        total = 0  # biến lưu tổng kết quả
        for i in range(1, n + 1):  
            # duyệt từ 1 đến n
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                # nếu chia hết cho 3 hoặc 5 hoặc 7
                total += i  
        return total  # trả kết quả