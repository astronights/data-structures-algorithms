# 1-D DP Solutions

class Solution:
	# Solution Functions

	def climbStairs(self, n: int) -> int:
		'''Ways to Climb Stairs

  		Space Complexity: O(1) -> Constants
    		Time Complexity: O(n) -> Single Pass

      		Args:
			n (int): Stairs to climb

   		Returns:
     			ways (int): Number of ways
		'''
        	if n < 2:
            		return 1
        	
		prev, ways = 1, 1
        	for _ in range(n - 1):
            		prev, ways = ways, prev + ways
        	
		return ways
