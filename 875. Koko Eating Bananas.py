class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Define the search space: 1 is minimum speed, max(piles) is the fastest needed
        l, r = 1, max(piles)

        while l < r:
            # k is the candidate speed
            k = (l + r) // 2
            
            # Calculate total hours spent eating at speed k
            hours_spent = 0
            for p in piles:
                # Use math.ceil for the "wait for next hour" rule
                hours_spent += math.ceil(p / k)
            
            # Binary Search Logic
            if hours_spent <= h:
                # If we finish in time, k is a candidate, but try to find a SLOWER speed
                r = k
            else:
                # If we take too long, we MUST go faster
                l = k + 1
        
        # l and r will converge on the minimum integer k
        return l