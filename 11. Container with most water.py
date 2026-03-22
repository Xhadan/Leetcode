class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        L = 0
        R = n-1
        max_area = 0

        while L<R:
            width = R-L
            h = min(height[L], height[R])
            area = width * h
            max_area = max(area, max_area) 

            # Move the pointer pointing to the shorter bar
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return max_area
    


        