class Solution:
    def divideArray(self, nums):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for v in count.values():
            if v % 2 != 0:
                return False

        return True