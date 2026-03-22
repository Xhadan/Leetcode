class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # 1. Update the minimum price we've seen so far
            if price < min_price:
                min_price = price
            
            # 2. Calculate profit if we sold at the current price
            current_profit = price - min_price
            
            # 3. Update our record max profit
            if current_profit > max_profit:
                max_profit = current_profit
                
        return max_profit