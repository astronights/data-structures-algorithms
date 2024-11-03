# Binary Search Solutions

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
