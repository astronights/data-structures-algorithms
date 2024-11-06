# Sliding Window Solutions

class Solutions:
	# Solution Functions

	def maxProfit(self, prices: List[int]) -> int:
		'''Calculate maximum profit

  		Space Complexity: O(1) -> Max / Min Values
    		Time Complexity: O(n) -> Single Pass

      		Args:
			prices (list): Iterable of prices

   		Returns:
     			max_profit (int): Maximum profit
		'''
		max_profit = 0
        	min_price = prices[0]
        	
        	for price in prices[1:]:
            		max_profit = max(max_profit, price - min_price)
            		min_price = min(min_price, price)
        	return max_profit 

	def lengthOfLongestSubstring(self, s: str) -> int:
		'''Length of longest substring without duplicates

  		Space Complexity: O(n) -> Frequency dictionary
    		Time Complexity: O(n) -> Single Pass over characters

      		Args:
			s (str): Iterable of characters

   		Returns:
     			longest (int): Length of longest string
		'''
        	ix = 0
        	longest = 0
		seen = {}
		
        	for i, c in enumerate(s):
            		if seen.get(c, 0) == 0:
                		seen[c] = 1
                		longest = max(longest, i - ix + 1)
            		else:
                		while seen[c] != 0:
                    			seen[s[ix]] -= 1
                    			ix += 1
                		seen[c] = 1
        	return longest

	def characterReplacement(self, s: str, k: int) -> int:
		'''Longest repeating substring with character replacement

  		Space Complexity: O(1) -> Frequency counter [Size 26]
    		Time Complexity: O(n) -> Single Pass

      		Args:
			s (str): Iterable of characters
   			k (int): Maximum replacements

      		Returns:
			res (int): Longest substring
   		'''
    		
        	seen = {}
        	res = 0
        
		ix = 0
        	max_freq = 0

        	for i, c in enumerate(s):
            		seen[c] = seen.get(c, 0) + 1
            		max_freq = max(max_freq, seen[c])

            		while (i - ix + 1) - max_freq > k:
                		seen[s[ix]] -= 1
                		ix += 1
            		res = max(res, i - ix + 1)
			
        	return res

	def checkInclusion(self, s1: str, s2: str) -> bool:
		'''Check permutation of one string in another

  		Space Complexity: O(1) -> Counters of size 26
    		Time Complexity: O(n) -> Two Pass over string

      		Args:
			s1 (str): String to check against
   			s2 (str): String to check within

      		Returns:
			is_perm (bool): If permutation exists
   		'''
        	need = Counter(s1)
        	rem = Counter(s1)

        	ix = 0

        	for i, c in enumerate(s2):
			# Char is needed and not yet seen
            		if c in rem:
                		rem[c] -= 1
                		if rem[c] == 0:
                    			del rem[c]
           		else:
				# Char is needed but already seen
                		if c in need:
                    			while c not in rem:
                        			pc = s2[ix]
                        			if pc in need:
                            				rem[pc] = rem.get(pc, 0) + 1
                        			ix += 1
                    			del rem[c]
                		# Character not needed
				else:
                    			ix += 1
                    			rem = need.copy()
            		if not rem:
                		return True
		return False
            
	def minWindow(self, s: str, t: str) -> str:
		'''Minimum window with characters

  		Space Complexity: O(n) -> Frequency Counters
    		Time Complexity: O(n) -> Single Pass

      		Args:
			s (str): String	
   			t (str): Substring

      		Returns:
			shortest (str): Minimum window
   		'''
        	need = Counter(t)
        	rem = Counter(t)

		ix = 0
        	seen = {}
        	shortest = s + s

        	for i, c in enumerate(s):
			# Mark latest seen instance
            		if c in need:
                		seen[c] = i
            		if c in rem:
                		rem[c] -= 1
            		else:
				# Slide window
                		if c in need and s[ix] == c:
                    			ix = min(seen.values())
            		if rem[c] == 0:
                		del rem[c]
            
            		if len(rem) == 0:
                		while s[ix] not in need:
                    			ix += 1
                		if (i - ix + 1) < len(shortest):
                    			shortest = s[ix:i+1]
					
        	return shortest if len(shortest) <= len(s) else ''
