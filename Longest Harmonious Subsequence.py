class Solution:
    def findLHS(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        res = 0
        for num in count:
            if num + 1 in count:
                res = max(res, count[num] + count[num + 1])
        return res