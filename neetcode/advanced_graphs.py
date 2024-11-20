# Advanced Graphs Solutions
import heapq
from collections import defaultdict

class Solution:
	# Solution Functions

	def findItinerary(self, tickets: List[List[str]]) -> List[str]:
		'''Build complete Itinerary

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

	def minCostConnectPoints(self, points: List[List[int]]) -> int:
		'''Minimum cost to connect all points

  		Space Complexity: O(n ^ 2) -> Min Heap of All Pairs
    		Time Complexity: O (n ^ 2 * log n) -> All Pairs Heap IO

      		Args:
			points (list): Iterable of co-ordinates

   		Returns:
     			cost (int): Minimum cost
		'''
        	n = len(points)
        	dists = defaultdict(list)
        
		for i in range(n):
            		for j in range(i+1, n):
                		a, b = points[i]
                		x, y = points[j]
				d = abs(a-x) + abs(b-y)
                
				dists[i].append((d, j))
                		dists[j].append((d, i))

        	cost = 0
        	seen = set()
        	min_heap = [(0, 0)]

        	while len(seen) < n:
            		d, cur = heapq.heappop(min_heap)

            		if cur in seen:
                		continue
            
            		cost += d
            		seen.add(cur)

            		for p in dists[cur]:
                		heapq.heappush(min_heap, p)
        	return cost
