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

	def hammingWeight(self, n: int) -> int:
		'''Count number of 1 bits

  		Space Complexity: O(1) -> Counter
    		Time Complexity: O(n) -> Single Pass

      		Args:
			n (int): Number

   		Returns:
     			c (int): Number of one bits
		'''
        	c = 0
        	while n:
            		n = n & (n - 1)
            		c += 1
        	return c

	def countBits(self, n: int) -> List[int]:
		'''Count 1 bits in all numbers

  		Space Complexity: O(n) -> Result
    		Time Complexity: O(n) -> Single Pass

      		Args:
			n (int): Range of numbers

   		Returns:
     			out (list): 1 Bit Counts
		'''
        	ix = 2
        	out = [0]
        
		for i in range(1, n + 1):
			out.append(1 + out[i - ix])
			
            		if i == ix:
                		ix *= 2
        	return out

 	def reverseBits(self, n: int) -> int:
		'''Reverse Bits

  		Space Complexity: O(1) -> Single number
    		Time Complexity: O(1) -> 32 bit iteration

      		Args:
			n (int): Input number

   		Returns:
     			out (int): Number with reversed bits
		'''
       		out = 0
        	
		for i in range(32):
            		bit = (n >> i) & 1
            		out += (bit << (31 - i))
        	return out
