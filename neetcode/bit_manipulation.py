# Bit Manipulation Solutions
import math

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

	def missingNumber(self, nums: List[int]) -> int:
		'''Find missing number from range of numbers

  		Space Complexity: O(1) -> Single number
    		Time Complexity: O(n) -> Single Pass

      		Args:
			nums (list): Iterable of numbers

   		Returns:
     			res (int): Missing number
		'''
        	res = 0
        	for i, n in enumerate(nums):
            		res += i + 1 - n
        	return res

	def getSum(self, a: int, b: int) -> int:
		'''Sum of two numbers without +

  		Space Complexity: O(1) -> Constants
    		Time Complexity: O(1) -> Bit iteration

      		Args:
			a (int): Number 1
   			b (int): Number 2

      		Returns:
			total (int): Sum of numbers
   		'''
        	mask = 0xFFFFFFFF
        	MAX_INT = 0x7FFFFFFF
        
        	while b != 0:
            		carry = (a & b) << 1
            		a = (a ^ b) & mask
            		b = carry & mask

        	return a if a <= MAX_INT else ~(a ^ mask)

	def reverse(self, x: int) -> int:
		'''Reverse number without going out of 32 bit bounds

  		Space Complexity: O(1) -> Single numbers
    		Time Complexity: O(1) -> Number digit iteration

      		Args:
			x (int): Number

   		Returns:
     			out (int): Reversed number
		'''
        	MIN = - 2 ** 31
        	MAX = 2 ** 31 - 1
		
        	out = 0
        
		while x != 0:
            		remainder = int(math.fmod(x, 10))
            		x = int(x / 10)

            		if out > MAX // 10 or (out == MAX // 10 and remainder > MAX % 10):
                		return 0
            		elif out < MIN // 10 or (out == MIN // 10 and remainder < MIN % 10):
                		return 0
            		out = out * 10 + remainder
        	return out 
