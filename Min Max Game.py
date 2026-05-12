class Solution:
    def minMaxGame(self, nums):
        # lặp cho đến khi mảng còn 1 phần tử
        while len(nums) > 1:
            n = len(nums)
            newNums = [0] * (n // 2)  # mảng mới có kích thước n/2
            for i in range(n // 2):
                a = nums[2 * i]       # phần tử thứ nhất của cặp
                b = nums[2 * i + 1]   # phần tử thứ hai của cặp
                if i % 2 == 0:
                    newNums[i] = min(a, b)  # index chẵn → lấy min
                else:
                    newNums[i] = max(a, b)  # index lẻ → lấy max
            nums = newNums  # thay thế mảng cũ bằng mảng mới
        return nums[0]  # phần tử cuối cùng