class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        # Initialize result with 0s
        res = [0] * n
        # Stack will store indices
        stack = []

        for i in range(n):
            # Check if current temp is greater than the temp at top of stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            
            # Always push current index to look for its future warmer day
            stack.append(i)

        return res