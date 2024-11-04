# Sliding Window Solutions
from collections import defaultdict

class Solutions:
	# Solution Functions

	def maxProfit(self, prices: List[int]) -> int:
		'''Calculate maximum profit

  		Space Complexity: O(1) -> Max / Min Values
    		Time Complexity: O(n) -> Single Pass

      		Args:
			prices (list): Iterable of prices

   		Returns:
     			max_profit (int): Maximum profit
		'''
		max_profit = 0
        	min_price = prices[0]
        	
        	for price in prices[1:]:
            		max_profit = max(max_profit, price - min_price)
            		min_price = min(min_price, price)
        	return max_profit 
