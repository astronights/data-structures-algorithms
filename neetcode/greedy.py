# Greedy Solutions
from collections import Counter

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

	def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
		'''Is hand of straights

  		Space Complexity: O(n) -> Frequency Counter
    		Time Complexity: O(n) -> Single Pass

      		Args:
			hand (list): Iterable of values
   			groupSize (int): Size of straight

      		Returns:
			is_straight (bool): If hand of straights exists
   		'''
		if len(hand) % groupSize != 0:
            		return False
        
		count = Counter(hand)

        	for card in hand:
			if count.get(card, 0) == 0:
                		continue

			# Get the earliest card in sequence
			start = card
            		while count.get(start - 1, 0) > 0:
                		start -= 1
            
			# Check the sequence
			for i in range(start, start + groupSize):
                		if count.get(i, 0) == 0:
                    			count[i] -= 1
                		else:
                    			return False

        	return True

	def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
		'''Possibility to Merge Triplets

  		Space Complexity: O(1) -> Triplet tuple
    		Time Complexity: O(n) -> Single Pass

      		Args:
			triplets (list): Iterable of triplets
   			target (list): Target triplet

       		Returns:
	 		is_target (bool): If target is attainable
    		'''
        	x, y, z = target
        	cur = [0, 0, 0]
        
		for triple in triplets:
            		a, b, c = triple
            		if a <= x and b <= y and c <= z:
                		cur = [max(a, cur[0]), max(b, cur[1]), max(c, cur[2])]
        	
		return cur == target

	def partitionLabels(self, s: str) -> List[int]:
		'''Partition labels

  		Space Complexity: O(n) -> Last Seen Counter
    		Time Complexity: O(n) -> Single Pass

      		Args:
			s (str) -> Iterable of characters

   		Returns:
     			parts (list): Partition counts
		'''
        	seen = {}
        	for i, c in enumerate(s):
            		seen[c] = i

        	sofar = 0
        	prev = 0
        	parts = []

        	for i, c in enumerate(s):
            		sofar = max(sofar, seen[c])

            		if i == sofar:
                		parts.append(i - prev + 1)
                		prev = i + 1
        	return parts

	def checkValidString(self, s: str) -> bool:
		'''Check valid parenthesis string with wildcard

    		Space Complexity: O(1) -> Greedy Pointers
      		Time Complexity: O(n) -> Single Pass

 		Args:
   			s (str) -> Iterable of characters

		Returns:
  			is_valid (bool) -> If string can be valid
     		'''
		# Keeping track of min and max open parentheses
        	left_min = 0
        	left_max = 0

        	for c in s:
            		if c == '(':
                		left_min += 1
                		left_max += 1
            		elif c == ')':
                		left_min -= 1
                		left_max -= 1
            		else:
                		left_min -= 1
                		left_max += 1
            
            		if left_max < 0:
                		return False
            		if left_min < 0:
                		left_min = 0
        	
		return left_min == 0
