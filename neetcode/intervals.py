# Intervals Solutions

class Solution:
	# Solution Functions
	
	def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
		'''Insert New Interval

  		Space Complexity: O(n) -> Number of intervals
    		Time Complexity: O(n) -> Single Pass

      		Args:
			intervals (list): Iterable of intervals
   			newInterval (list): New Interval time

      		Returns:
			out (list): Updated intervals
   		'''
        	out = []
		start, end = newInterval
        
		for i, interval in enumerate(intervals):
            		ix_start, ix_end = interval
            
			if ix_end < start:
                		out.append(interval)
            		elif ix_start > end:
                		out.append([start, end])
                		return out + intervals[i:]
            		else:
                		start = min(start, ix_start)
                		end = max(end, ix_end)
        
        	return out + [[start, end]]
