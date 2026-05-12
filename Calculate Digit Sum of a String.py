class Solution:
    def digitSum(self, s, k):
        # lặp cho đến khi độ dài s <= k
        while len(s) > k:
            new_s = ""  # chuỗi mới sau mỗi vòng
        # chia s thành các nhóm độ dài k
            for i in range(0, len(s), k):
                group = s[i:i + k]  # lấy 1 nhóm
                digit_sum = 0  # tổng chữ số của nhóm
                for ch in group:
                    digit_sum += int(ch)  # cộng từng chữ số
                new_s += str(digit_sum)  # nối kết quả vào chuỗi mới
            s = new_s  # cập nhật lại s cho vòng tiếp theo
        return s  # khi độ dài <= k thì dừng