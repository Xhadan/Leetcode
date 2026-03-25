class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        
        # While l < r ensures we converge on a single element
        while l < r:
            mid = (l + r) // 2
            
            # If mid element is greater than right element, 
            # the minimum is strictly to the right
            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, the minimum is either at mid or to the left
            else:
                r = mid
                
        # Both l and r will eventually point to the minimum
        return nums[l]
        