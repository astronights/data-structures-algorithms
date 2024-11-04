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

	def lengthOfLongestSubstring(self, s: str) -> int:
		'''Length of longest substring without duplicates

  		Space Complexity: O(n) -> Frequency dictionary
    		Time Complexity: O(n) -> Single Pass over characters

      		Args:
			s (str): Iterable of characters

   		Returns:
     			longest (int): Length of longest string
		'''
        	start = 0
        	longest = 0
		seen = defaultdict(int)
		
        	for i, c in enumerate(s):
            		if seen.get(c, 0) == 0:
                		seen[c] += 1
                		longest = max(longest, i - ix + 1)
            		else:
                		while seen.get(c) != 0:
                    			seen[s[ix]] -= 1
                    			ix += 1
                		seen[c] = 1
        	return longest
