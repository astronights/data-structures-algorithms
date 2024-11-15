# Greedy Solutions

class Solution:
	# Solution Functions

	def maxSubArray(self, nums: List[int]) -> int:
		'''Maximum sum of sub array

  		Space Complexity: O(1) -> Maximum and current sum
    		Time Complexity: O(n) -> Single Pass

      		Args:
			nums (list): Iterable of numbers

   		Returns:
     			max_sum (int): Maximum sum
		'''
        	max_sum = -10001
        	cur_sum = 0
        
		for n in nums:
            		cur_sum += n
            		max_sum = max(max_sum, cur_sum)
            		if cur_sum < 0:
                		cur_sum = 0
        	return max_sum
