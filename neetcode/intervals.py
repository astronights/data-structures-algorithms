# Intervals Solutions

class Interval(object):
	
	def __init__(self, start: int, end: int):
		'''Interval Class

     		Args:
       			start (int): Beginning of interval
	  		end (int): End of interval
     		'''
        	self.start = start
        	self.end = end

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

	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		'''Merge Intervals

  		Space Complexity: O(n) -> New Interval List
    		Time Complexity: O(n log n) -> Tim Sort

      		Args:
			intervals (list): Iterable of intervals

   		Returns:
     			res (list): Merged intervals
		'''
        	intervals.sort()
        	res = [intervals[0]]

        	for start, end in intervals[1:]:
            		if start <= res[-1][1]:
                		res[-1][1] = max(res[-1][1], end)
            		else:
                		res.append([start, end])
        	return res

	def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
		'''Count Minimum non-overlapping intervals

  		Space Complexity: O(n) -> Tim Sort
    		Time Complexity: O(n log n) -> Tim Sort

      		Args:
			intervals (list): Iterable of intervals

   		Returns:
     			count (int): Number of intervals to remove
		'''
        	prev = -50001
		count = 0

        	intervals.sort(key=lambda pair: pair[1])
        
        	for start, end in intervals:
            		if start < prev:
                		count += 1
            		else:
                		prev = end
        	return count

	def canAttendMeetings(self, intervals: List[Interval]) -> bool:
		'''Check if meetings are not overlapping

  		Space Complexity: O(n) -> Tim Sort
    		Time Complexity: O(n log n) -> Tim Sort

      		Args:
			intervals (list): Iterable of intervals

   		Returns:
			can_attend (bool): If no overlap in meetings
   		'''
		prev = -1
        	intervals.sort(key=lambda x: x.start)
        
		for interval in intervals:
            		if interval.start < prev:
                		return False
            		prev = interval.end
        	return True
