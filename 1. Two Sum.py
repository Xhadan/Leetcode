class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for position, value in enumerate(nums): 
            complement = target - value

            if complement in prevMap:
             return [prevMap[complement], position]

            prevMap[value] = position