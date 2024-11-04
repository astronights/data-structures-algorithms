# Binary Search Solutions
from math import ceil

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
