class Solution:
    def buyChoco(self, prices, money):
        min1 = float('inf')  # giá nhỏ nhất
        min2 = float('inf')  # giá nhỏ nhì

        for p in prices:
            if p < min1:
                min2 = min1      # đẩy min1 cũ xuống min2
                min1 = p         # cập nhật min1 mới
            elif p < min2:
                min2 = p         # cập nhật min2 nếu p nằm giữa min1 và min2

        total = min1 + min2      # tổng 2 giá rẻ nhất

        return money - total if total <= money else money  
        # nếu đủ tiền → trả tiền dư, không đủ → giữ nguyên tiền