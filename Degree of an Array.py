class Solution:
    def findShortestSubArray(self, nums):
        count = {}
        first = {}
        last = {}
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1
        degree = max(count.values())
        res = len(nums)
        for num in count:
            if count[num] == degree:
                res = min(res, last[num] - first[num] + 1)
        return res