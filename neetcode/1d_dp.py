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

	def minCostClimbingStairs(self, cost: List[int]) -> int:
		'''Minimum cost to climb stairs

  		Space Complexity: O(n) -> DP Array
    		Time Complexity: O(n) -> Single Pass

      		Args:
			cost (list): Iterable of costs

   		Returns:
     			min_cost (int): Minimum cost to climb stairs
		'''
        	out = [0] * (len(cost) + 1)
        	
		for i in range(2, len(cost) + 1):
            		out[i] = min(cost[i-1] + out[i-1], cost[i-2] + out[i-2])
        	return out[-1]

	def rob(self, nums: List[int]) -> int:
		'''Maximum money obtained from non-consecutive houses

  		Space Complexity: O(n) -> DP Array
    		Time Complexity: O(n) -> Single Pass

		Args:
  			nums (list): Iterable of money available

     		Returns:
       			max_money (int): Maximum money obtainable
	  	'''
        	if len(nums) < 2:
            		return max(nums) if nums else 0
        
		money = [0] * len(nums)
        	money[0] = nums[0]
        	money[1] = max(nums[:2])
        
		for i in range(2, len(nums)):
            		money[i] = max(money[i-1], money[i-2] + nums[i])
        	return money[-1]

	def rob_round(self, nums: List[int]) -> int:
		'''Maximum money obtained from circular arrangement of houses

  		Space Complexity: O(n) -> DP Array
    		Time Complexity: O(n) -> Single Pass (Twice)

      		Args:
			nums (list): Iterable of available money

   		Returns:
     			max_money (int): Maximum money obtained
		'''
        	return max(nums[0], self.rob(nums[1:]), self.rob(nums[:-1]))

	def longestPalindrome(self, s: str) -> str:
		'''Longest Palindrome

    		Space Complexity: O(n) -> Palindrome string
      		Time Complexity: O(n ^ 2) -> Iterating over all possibilities

 		Args:
   			s (str): Iterable of characters to inspect

      		Returns:
			longest (str): Longest palindrome
   		'''
        	longest = ''

		# Odd Lengths
        	for ix in range(len(s)):
            		side = 0
            		while ix - side >= 0 and ix + side < len(s):
                		cur = s[(ix - side): (ix + side + 1)]
                		if cur == cur[::-1]:
                    			side += 1
                    			if len(cur) > len(longest):
                        			longest = cur
                		else:
                    			break
		# Even Lengths
        	for ix in range(1, len(s)):
            		side = 0
            		while ix - side >= 0 and ix + side <= len(s):
                		cur = s[(ix - side): (ix + side)]
                		if cur == cur[::-1]:
                    			side += 1
                    			if len(cur) > len(longest):
                        			longest = cur
                		else:
                    			break
        	return longest

	def countSubstrings(self, s: str) -> int:
		'''Count Palindromic substrings

  		Space Complexity: O(n) -> Palindrome string
      		Time Complexity: O(n ^ 2) -> Iterating over all possibilities

 		Args:
   			s (str): Iterable of characters to inspect

      		Returns:
			c (int): Number of palindromes
   		'''
        	c = 0

		# Odd lengths
        	for ix in range(len(s)):
            		side = 0
            		while ix - side >= 0 and ix + side < len(s):
                		cur = s[(ix - side): (ix + side + 1)]
                		if cur == cur[::-1]:
                    			side += 1
                    			c += 1
                		else:
                    			break
		# Even Lengths
        	for ix in range(1, len(s)):
            		side = 1
            		while ix - side >= 0 and ix + side <= len(s):
                		cur = s[(ix - side): (ix + side)]
                		if cur == cur[::-1]:
                    			side += 1
                    			c += 1
                		else:
                    			break
        	return c

	def numDecodings(self, s: str) -> int:
		'''Number of ways to decode string

    		Space Complexity: O(n) -> DP Array
      		Time Complexity: O(n) -> Single Pass

  		Args:
    			s (str): Iterable of numbers

       		Returns:
	 		n_ways (int): Number of ways
    		'''
		n = len(s)
        	ways = [0] * (n + 1)
		
        	ways[-1] = 1
            	for i in range(n - 1, -1, -1):
            		if s[i] != '0':
                		ways[i] = ways[i+1]
                		if i < n - 1 and int(s[i: i + 2]) < 27:
                    			ways[i] += ways[i + 2]
        	return ways[0]

	def coinChange(self, coins: List[int], amount: int) -> int:
		'''Minimum number of coins required

  		Space Complexity: O(n) -> DP Array
    		Time Complexity: O(n * k) -> Iteration

      		Values: Amount (n), Number of coins (k)

 		Args:
   			coins (list): Iterable of available coins
      			amount (int): Amount to achieve

  		Returns:
    			min_coins (int): Minimum number of coins needed
       		'''
        	dp = [10001] * (amount + 1) # Maximum amount 10000
        	dp[0] = 0

        	for val in range(1, amount + 1):
            		for c in coins:
                		if c <= val:
                    			dp[val] = min(dp[val], dp[val - c] + 1)
        	
		return dp[-1] if dp[-1] < 10001 else -1

	def maxProduct(self, nums: List[int]) -> int:
		'''Maximum product of subarray

  		Space Complexity: O(1) -> Tracked maximums and minimums
    		Time Complexity: O(n) -> Single Pass

      		Args:
			nums (list): Iterable of numbers

   		Returns:
     			max_product (int): Maximum product
		'''
        	max_product = nums[0]
        	c_max = 1
        	c_min = 1

        	for n in nums:
            		temp_max = n * c_max
            		c_max = max(n, n * c_max, n * c_min)
            		c_min = min(n, temp_max, n * c_min)

            		max_product = max(max_product, c_max)
			
        	return max_product
