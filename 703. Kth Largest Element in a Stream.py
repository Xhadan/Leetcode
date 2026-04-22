import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        
        # Shrink heap to size K immediately
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Step 1: Add the new value
        heapq.heappush(self.min_heap, val)
        
        # Step 2: If we exceed size K, remove the smallest (the root)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # Step 3: The root of the Min-Heap is our Kth largest
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)