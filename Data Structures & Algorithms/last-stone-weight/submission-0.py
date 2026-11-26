class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            heaviest = -heapq.heappop(heap)
            second_heaviest = -heapq.heappop(heap)

            if heaviest != second_heaviest:
                heapq.heappush(heap, -(heaviest - second_heaviest))

        return -heap[0] if heap else 0
        