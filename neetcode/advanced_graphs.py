# Advanced Graphs Solutions
from collections import defaultdict

class Solution:
	# Solution Functions

	def findItinerary(self, tickets: List[List[str]]) -> List[str]:
		'''Find Itinerary

  		Space Complexity: O(n) -> Number of edges
    		Time Complexity: O(n log n) -> Tim Sort

      		Args:
			tickets (list): Ticket edges

   		Returns:
     			route (list): Itinerary
		'''
        	paths = defaultdict(list)
        
		for src, dst in tickets:
            		paths[src].append(dst)
		for src in paths:
            		paths[src].sort(reverse=True)

        	stack = ['JFK']
        	route = []

        	while stack:
            		cur = stack[-1]
            		if paths[cur]:
                		stack.append(paths[cur].pop())
            		else:
                		route.append(stack.pop())

        	return route[::-1]
