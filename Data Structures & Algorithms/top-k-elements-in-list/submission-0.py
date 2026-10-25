from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        
        for num in nums:
            frequencies[num] += 1


        heap = []
        for elem in frequencies:
            heapq.heappush(heap, (frequencies[elem], elem))

            if len(heap) > k:
                heapq.heappop(heap)






        result = []
        for i in range(k):
            if i >= len(heap):
                break
            result.append(heap[i][1])

        return result
        