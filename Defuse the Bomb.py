class Solution:
    def decrypt(self, code, k):
        n = len(code)

        if k == 0:
            return [0] * n  # nếu k = 0 → tất cả = 0

        res = [0] * n  # mảng kết quả

        for i in range(n):
            total = 0  # tổng cho phần tử i

            if k > 0:
                # cộng k phần tử phía sau (circular)
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
            else:
                # cộng |k| phần tử phía trước (circular)
                for j in range(1, -k + 1):
                    total += code[(i - j) % n]

            res[i] = total  # gán kết quả

        return res