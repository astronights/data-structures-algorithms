# Two Pointers Solutions

class Solutions:
	# Solution Functions
	
	def isPalindrome(self, s: str) -> bool:
		'''Check if a string is a palindrome

  		Space Complexity: O(n) -> Cleaned string
    		Time Complexity: O(n) -> Iteration to half the string

      		Args:
			s (str): String

   		Returns:
     			is_pal (bool): Palindrome check
		'''
	        s = [c.lower() for c in s if c.isalnum()]
        	l, r = 0, len(s) - 1
		
        	while l < r:
            		if s[l] == s[r]:
		                l += 1
		                r -= 1
		        else:
		        	return False
		return True

	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		'''Get indices of two sum in sorted array

  		Space Complexity: O(1) -> Pointers
    		Time Complexity: O(n) -> Iteration over elements

      		Args:
			numbers (list): Iterable of numbers
   			target (int): Target sum

      		Returns:
			indices (list): Indices of elements
   		'''
        	l, r = 0, len(numbers) - 1
        
		while l < r:
			cur_sum = numbers[l] + numbers[r]
            		if cur_sum == target:
                		return [l+1, r+1]
            		elif cur_sum < target:
                		l += 1
            		else:
                		r -= 1
		return [-1, -1]

	def threeSum(self, nums: List[int]) -> List[List[int]]:
		'''Get all sets of 3 elements that sum to 0

  		Space Complexity: O(n) -> Sorting
    		Time Complexity: O(n^2) -> Two Sum for each element

      		Args:
			nums (list): Iterable of numbers

   		Returns:
     			res (list): List of solutions
		'''
        	res = []
        	nums.sort()

        	for i, n in enumerate(nums):
			# Conditions to exit / skip iteration
            		if n > 0:
                		break
            		if i > 0 and n == nums[i-1]:
                		continue
            
            		l, r = i + 1, len(nums) - 1
			while l < r:
                		threesum = n + nums[l] + nums[r]

                		if threesum == 0:
                    			res.append([n, nums[l], nums[r]])
                    			l += 1
                    			r -= 1
                    			while nums[l] == nums[l-1] and l < r:
                        			l += 1
                		elif threesum < 0:
                    			l += 1
                		else:
                    			r -= 1
        	return res

	def maxArea(self, heights: List[int]) -> int:
		'''Maximum area of water container

  		Space Complexity: O(1) -> Maximum height + Pointers
    		Time Complexity: O(n) -> Iterating over all heights

  		Args:
    			heights (list): Container boundaries

       		Returns:
	 		max_area (int): Maximum area
    		'''
        	max_area = 0
        	l, r = 0, len(heights) - 1

        	while l < r:
            		area = min(heights[l], heights[r]) * (r-l)
	 	        max_area = max(max_area, area)

            		if heights[l] < heights[r]:
                		l += 1
            		else:
                		r -= 1
        	return max_area

	def trap(self, height: List[int]) -> int:
		'''Amount of trapped rainwater

  		Space Complexity: O(1) -> Pointers + Total
    		Time Complexity: O(n) -> Iterating over all elements

      		Args:
			height (list): Heights of container

   		Returns:
     			rain (int): Total rain water
		'''
		rain = 0
		l, r = 0, len(height) - 1
		max_L, max_R = height[l], height[r]

		while l < r:
			if max_L < max_R:
				l += 1
				max_L = max(max_L, height[l])
				rain += max_L - height[l]
			else:
				r -= 1
				max_R = max(max_R, height[r])
				rain += max_R - height[r]
		return rain
