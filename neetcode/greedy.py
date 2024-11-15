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

	def canJump(self, nums: List[int]) -> bool:
		'''If possible jumps to the last index

  		Space Complexity: O(1) -> Pointer
    		Time Complexity: O(n) -> Single Pass

      		Args:
			nums (list): Iterable of jump distances

   		Returns:
     			can_jump (bool): If can reach last index
		'''
        	start = len(nums) - 1

        	for i in range(len(nums)-2, -1, -1):
            		if i + nums[i] >= start:
                		start = i
        	return start == 0

	def jump(self, nums: List[int]) -> int:
		'''Minimum number of jumps

  		Space Complexity: O(1) -> Pointers
    		Time Complexity: O(n) -> Single Pass

		Args:
  			nums (list): Iterable to jump distances

       		Returns:
	 		c (int): Minimum jumps
    		'''
        	c = 0
        	end = 0
        	sofar = -1

        	for i in range(len(nums) - 1):
            		sofar = max(sofar, i + nums[i])

            		if sofar >= len(nums) - 1:
                		return c + 1

            		if i == end:
                		c += 1
                		end = sofar
        	return 0

	def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
		'''Can Complete Circuit

  		Space Complexity: O(1) -> Tracking variables
    		Time Complexity: O(n) -> Single Pass

  		Args:
    			gas (list): Iterable of gas fillings
       			cost (list): Iterable of costs

   		Returns:
     			start (int): Start index
		''' 
        	if sum(gas) < sum(cost):
            		return -1
        
        	start = 0
        	cur_gas = 0
        
		for i in range(len(gas)):
            		cur_gas += gas[i] - cost[i]
            		if cur_gas < 0:
                		start = i + 1
                		cur_gas = 0
        	return start
