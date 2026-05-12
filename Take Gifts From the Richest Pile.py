import heapq
import math

class Solution:
    def pickGifts(self, gifts, k):
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            remaining = int(math.sqrt(largest))
            heapq.heappush(max_heap, -remaining)
        
        return -sum(max_heap)