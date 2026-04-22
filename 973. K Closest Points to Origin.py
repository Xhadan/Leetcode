import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Max-Heap to store the k closest points
        # Store as: (-distance, x, y)
        max_heap = []
        
        for x, y in points:
            # Calculate squared distance (skip sqrt for efficiency)
            dist = -(x**2 + y**2)
            
            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist, x, y))
            else:
                # If current point is closer than the "farthest" of the top k
                if dist > max_heap[0][0]:
                    heapq.heapreplace(max_heap, (dist, x, y))
        
        # Extract the points from the heap
        return [[x, y] for dist, x, y in max_heap]