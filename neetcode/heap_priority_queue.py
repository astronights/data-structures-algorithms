# Heap / Priority Queue Solutions
import math
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

  		Space Complexity: O(n) -> Stone Weight Heap
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


	def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
		'''K Closest Points to Origin

  		Space Complexity: O(k) -> Point Heap
    		Time Complexity: O(n log k) -> Heap IO

      		Args:
			points (list): Iterable of co-ordinates
   			k (int): Index of closest points

      		Returns:
			c_points (list): K Closest Points
   		'''
        	min_heap = []
        
		for p in points:
            		x, y = p[0], p[1]
            		d = math.sqrt(x**2 + y**2)
            		heapq.heappush(min_heap, (-d, x, y))

            		if len(min_heap) > k:
                		heapq.heappop(min_heap)

        	return [[p[1], p[2]] for p in min_heap]

	def findKthLargest(self, nums: List[int], k: int) -> int:
		'''Find K-th largest element in array

  		Space Complexity: O(k) -> Element Heap
    		Time Complexity: O(n log k) -> Heap IO

      		Args:
			nums (list): Iterable of elements
   			k (int): Index of largest element

      		Returns:
			elem (int): K-th largest element
   		'''
        	min_heap = []
        
		for n in nums:
            		heapq.heappush(min_heap, n)

            		if len(min_heap) > k:
                		heapq.heappop(min_heap)

        	return min_heap[0]
