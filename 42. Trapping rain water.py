class Solution:
    def trap(self, height: List[int]) -> int:
      
        if not height: return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                # Water trapped is the distance between current bar and the max wall
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                # Water trapped is the distance between current bar and the max wall
                res += rightMax - height[r]
                
        return res