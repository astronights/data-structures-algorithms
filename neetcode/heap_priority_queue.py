# Heap / Priority Queue Solutions
import heapq

class KthLargest:

	def __init__(self, k: int, nums: List[int]):
		'''K-th Largest element in stream

  		Space Complexity: O(k) -> Min Heap
    		Time Complexity: O(n) -> Heapify

      		Args:
			k (int): Index of largest element
   			nums (list): Stream of numbers
      		'''
		self.k = k
        	self.heap = nums[:]
        	
		heapq.heapify(self.heap)
        	while len(self.heap) > k:
            		heapq.heappop(self.heap)

	def add(self, val: int) -> int:
		'''Add Value to heap and return K-th largest

  		Time Complexity: O(log k) -> Heap IO

  		Args:
    			val (int): Value to add

       		Returns:
	 		kth (int): K-th largest number
    		'''
        	heapq.heappush(self.heap, val)
        	if len(self.heap) > self.k:
            		heapq.heappop(self.heap)
        	return self.heap[0]

class Solution:
	# Solution Functions
	
	def lastStoneWeight(self, stones: List[int]) -> int:
		'''Last Stone Weight after smashing

  		Space Complexity: O(n) -> Stone Iteration
    		Time Complexity: O(n log n) -> Heap IO

      		Args:
			stones (list): Iterable of weights

   		Returns:
     			out (int): Remaining stone
		'''
        	stones = [-x for x in stones]
        	heapq.heapify(stones)

        	while len(stones) > 1:
            		a = heapq.heappop(stones)
			b = heapq.heappop(stones)

            		diff = abs(a - b)
			if diff:
                		heapq.heappush(stones, -diff)

        	return -stones[0] if stones else 0
