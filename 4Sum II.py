class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        hashmap = {}
        
        for a in nums1:
            for b in nums2:
                s = a + b
                hashmap[s] = hashmap.get(s, 0) + 1
        
        count = 0
        
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                count += hashmap.get(target, 0)
        
        return count