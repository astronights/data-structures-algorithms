# Binary Search Solutions
from math import ceil
from collections import defaultdict

class Solutions:
	# Solution Functions

        def search(self, nums: List[int], target: int) -> int:
                '''Binary Search in a list

                Space Complexity: O(1) -> Pointers
                Time Complexity: O(log n) -> Binary Search

                Args:
                        nums (list): Iterable of numbers
                        target (int): Number to find

                Returns:
                        mid (int): Index of solution
                '''
                l, r = 0, len(nums) - 1

                while l <= r:
                        mid = (l + r) // 2

                        if nums[mid] == target:
                                return mid
                        elif nums[mid] < target:
                                l = mid + 1
                        else:
                                r = mid - 1
                return -1

	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		'''Search element in matrix

  		Space Complexity: O(n) -> Pointers
    		Time Complexity: O(log (m*n)) -> Binary Search

      		Values: Dimensions of matrix (m*n)

 		Args:
   			matrix (list): 2 Dimensional list of values
      			target (int): Target to find

  		Returns:
    			is_exist (bool): If value in matrix
       		'''
		M, N = len(matrix), len(matrix[0])
        	l, r = 0, M * N - 1

        	while l <= r:
            		mid = (l + r) // 2
            		mid_R, mid_C = mid // N, mid % N
			
            		if matrix[mid_R][mid_C] == target:
                		return True
            		elif matrix[mid_R][mid_C] < target:
                		l = mid + 1
            		else:
                		r = mid - 1
        	return False

	def minEatingSpeed(self, piles: List[int], h: int) -> int:
        	'''Minimum eating speed to eat bananas

  		Space Complexity: O(1) -> Pointers
    		Time Complexity: O(log n) -> Binary Search

      		Values: Size of highest pile (n)

      		Args:
			piles (list): Piles of bananas
   			h (int): Maximum permissible time

		Returns:
  			k (int): Minimum eating speed
     		'''
		l, r = 1, max(piles)
        	k = float('inf')
        	
		while l <= r:
            		mid = (l + r) // 2

            		t_time = sum(ceil(float(p) / mid) for p in piles)

	    		if t_time <= h:
                		k = mid
                		r = mid - 1
            		else:
                		l = mid + 1
        	return int(k)

	def findMin(self, nums: List[int]) -> int:
		'''Minimum in a rotated sorted array

  		Space Complexity: O(1) -> Pointers
    		Time Complexity: O(log n) -> Binary Search

      		Args:
			nums (list): Iterable of numbers

   		Returns:
     			val (int): Minimum value
		'''
	        l, r = 0, len(nums) - 1

        	while l < r:
            		# Mid Calculation different
			mid = l + (r - l) // 2

            		if nums[mid] < nums[r]:
				r = mid
			else:
				l = mid + 1
	        return nums[l]

	def search(self, nums: List[int], target: int) -> int:
		'''Search in a rotated sorted array

  		Space Complexity: O(1) -> Pointers
    		Time Complexity: O(log n) -> Binary Search

      		Args:
			nums (list): Iterable of numbers
   			target (int): Number to find

      		Returns:
			index (int): Index of target
   		'''
	        l, r = 0, len(nums) - 1

        	while l <= r:
            		mid = (l + r) // 2
            
			if nums[mid] == target:
                		return mid
            		elif nums[l] <= nums[mid]:
                		if target >= nums[l] and target < nums[mid]:
                    			r = mid - 1
                		else:
                    			l = mid + 1
            		else:
                		if target <= nums[r] and target > nums[mid]:
                    			l = mid + 1
                		else:
                    			r = mid - 1
        	return -1

	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		'''Median of two sorted arrays

    		Space Complexity: O(1) -> Pointers
      		Time Complexity: O(log min(m, n)) -> Binary Search on shorter list

 		Values: Length of lists (m, n)

   		Args:
     			nums1 (list): Iterable 1 of numbers
			nums2 (list): Iterable 2 of numbers

   		Returns:
     			mid (float): Median value
		'''
        	if len(nums1) > len(nums2):
			nums1, nums2 = nums2, nums1

        	half = (len(nums1) + len(nums2)) // 2

        	l_a, r_a = 0, len(nums1) - 1

        	while True:
            		mid_A = (l_a + r_a) // 2
            		mid_B = half - 1 - mid_A - 1

            		left_A = nums1[mid_A] if mid_A >= 0 else float('-inf')
			right_A = nums1[mid_A + 1] if mid_A + 1 < len(nums1) else float('inf')

            		left_B = nums2[mid_B] if mid_B >= 0 else float('-inf')
            		right_B = nums2[mid_B + 1] if mid_B + 1 < len(nums2) else float('inf')

            		if left_A <= right_B and right_A >= left_B:
                		if all_len % 2 == 0:
                    			return (max(left_A, left_B) + min(right_A, right_B)) / 2
                		else:
                    			return min(right_A, right_B)
            		elif left_A > right_B:
                		r_a = mid_A - 1
            		else:
                		l_a = mid_A + 1



class TimeMap:

	def __init__(self):
		'''Time Based Key Value Store

		Space Complexity: O(m*n) -> Timestamps for keys

    		Values: Maximum number of timestamps (m), Unique keys (n)
      		'''
        	self.log = defaultdict(list)

    	def set(self, key: str, value: str, timestamp: int) -> None:
		'''Add value to store

    		Time Complexity: O(1) -> List Append

      		Args:
			key (str): String Key
   			value (str): String Value
      			timestamp (int): Time of insertion
	 	'''
	        self.log[key].append((timestamp, value))

	def get(self, key: str, timestamp: int) -> str:
		'''Get latest value by timestamp

  		Time Complexity: O(log m) -> Binary Search

      		Args:
			key (str): String key
   			timestamp (int): Timestamp

      		Returns:
			val (str): Latest value
   		'''
        	val = ''
		
	        if key in self.log:
	        	logs = self.log[key]
	        	l, r = 0, len(logs) - 1
			
	        	while l <= r:
	                	mid = (l + r) // 2
	                	cur_log = logs[mid]
				
	                	if cur_log[0] == timestamp:
	                    		val = cur_log[1]
	                    		break
	                	elif cur_log[0] < timestamp:
	                    		val = cur_log[1]
	                    		l = mid + 1
	                	else:
	                    		r = mid - 1
	        return val
