# Bit Manipulation Solutions

class Solution:
	# Solution Functions

	def singleNumber(self, nums: List[int]) -> int:
		'''Find only single number in list

  		Space Complexity: O(1) -> XOR Counter
		Time Complexity: O(n) -> Single Pass

  		Args:
    			nums (list): Iterable of numbers

       		Returns:
	 		x (int): Single number
    		'''
        	x = 0
        	for n in nums:
            		x ^= n
        	return x
