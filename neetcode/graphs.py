# Graphs Solutions
from collections import deque, defaultdict

class Node:
	def __init__(self, val = 0, neighbors = None):
		'''Graph Node

    		Args:
      			val (int): Node Value
	 		neighbors (list): Neighboring nodes
		'''
        	self.val = val
        	self.neighbors = neighbors if neighbors is not None else []

class Solution:
	# Solution Functions

	def numIslands(self, grid: List[List[str]]) -> int:
		'''Calculate number of islands

  		Space Complexity: O(m * n) -> Grid shape
    		Time Complexity: O(m * n) -> BFS

      		Values: Grid dimensions (m x n)

      		Args:
			grid (list): Geographical grid

    		Returns:
      			n_isles (int): Number of islands
	 	'''
        	n_isles = 0
        	R, C = len(grid), len(grid[0])
        	dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
		for i in range(R):
            		for j in range(C):
                		if grid[i][j] == '1':
                    			n_isles += 1
                    			seen = set()
                    			island = deque([(i, j)])
                    
					while island:
						# Explore current cell
                        			x, y = island.popleft()
                        			if (x, y) in seen:
                            				continue
                        			seen.add((x, y))
                        			grid[x][y] = '0'

						# Add neighbouring land cells to queue
						for dx, dy in dirs:
                            				nx, ny = x + dx, y + dy
                            				if (nx >= 0 and nx < R 
							    and ny >= 0 and ny < C 
							    and grid[nx][ny] == '1'):
                                				island.append((nx, ny))
        	return n_isles


	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		'''Maximum area of island

  		Space Complexity: O(m * n) -> Grid shape
    		Time Complexity: O(m * n) -> BFS

      		Values: Grid dimensions (m x n)

  		Args:
    			grid (list): Grid

       		Returns:
	 		max_area (int): Maximum area of island
    		'''
        	max_area = 0
        	seen = set()
        	R, C = len(grid), len(grid[0])
        	dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
		for i in range(R):
            		for j in range(C):
                		if grid[i][j] == 1:
                    			cur_area = 0
                    			queue = deque([(i, j)])

					# BFS
					while queue:
                        			x, y = queue.popleft()
                        			if (x, y) in seen:
                            				continue
                        			cur_area += 1
                        			seen.add((x, y))

                        			for dx, dy in dirs:
                            				nx, ny = x + dx, y + dy

                            				if (nx >= 0 and nx < R 
							    and ny >= 0 and ny < C 
							    and grid[nx][ny] == 1):
                                				queue.append((nx, ny))

                    			max_area = max(max_area, cur_area)
		return max_area

	def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
		'''Clone Graph

  		Space Complexity: O(V) -> V Nodes
    		Time Complexity: O(V + E) -> Nodes + Edges

      		Values: Vertices (V), Edges (E)

      		Args:
			node (Node): Graph Node

   		Returns:
     			copy_node (Node): Copied Graph Node
		'''		
        	if not node:
            		return None
        	nodes = {}
        	queue = deque([node])
        
		while queue:
            		cur = queue.popleft()
            		nodes[cur] = Node(cur.val)
            		
			for n in cur.neighbors:
                		if n not in nodes:
                    			queue.append(n)
        
        	for key in nodes.keys():
            		nodes[key].neighbors = [nodes[x] for x in key.neighbors]

        	return nodes[node]

	def islandsAndTreasure(self, grid: List[List[int]]) -> None:
		'''Distance to Treasure Chests

  		Space Complexity: O(m * n) -> Grid shape
    		Time Complexity: O(m * n) -> BFS

      		Values: Grid dimensions (m x n)

 		Args:
   			grid (list): Geaographical Grid
		'''
		queue = deque()
        	R, C = len(grid), len(grid[0])
        	
        	for i in range(R):
            		for j in range(C):
                		if grid[i][j] == 0:
                    			queue.append((i, j, 0))

		seen = set()
        	dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        	while queue:
            		x, y, d = queue.popleft()
            
            		if (x, y) in seen:
                		continue

			grid[x][y] = d
            		seen.add((x, y))

            		for dx, dy in dirs:
                		nx, ny = x + dx, y + dy
                
                	if (nx >= 0 and nx < R 
			    and ny >= 0 and ny < C 
			    and grid[nx][ny] == 2147483647):
                    		queue.append((nx, ny, d + 1))

	def orangesRotting(self, grid: List[List[int]]) -> int:
		'''Time to rot all fruits

  		Space Complexity: O(m * n) -> Grid shape
    		Time Complexity: O(m * n) -> BFS

      		Values: Grid dimensions (m x n)

 		Args:
   			grid (list): Grid of fruits

      		Returns:
			max_d (int): Time to rot
   		'''
        	n_fresh = 0
		queue = deque()
        	R, C = len(grid), len(grid[0])
        
        	for i in range(R):
            		for j in range(C):
                		if grid[i][j] == 1:
                    			n_fresh += 1
                		elif grid[i][j] == 2:
                    			queue.append((i, j, 0))

		max_d = 0
        	seen = set()
        	dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

	        while queue:
            		x, y, d = queue.popleft()

            		if (x, y) in seen:
                		continue

            		n_fresh -= min(1, d)
            		seen.add((x, y))

            		max_d = max(max_d, d)

            		for dx, dy in dirs:
                		nx, ny = x + dx, y + dy

                		if (nx >= 0 and nx < R 
				    and ny >= 0 and ny < C 
				    and grid[nx][ny] == 1):
                    			queue.append((nx, ny, d + 1))

        	return max_d if n_fresh == 0 else -1

	def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
		'''Pacific Atlantic Oceans Water Flow

		Space Complexity: O(m * n) -> Grid shape
    		Time Complexity: O(m * n) -> BFS

      		Values: Grid dimensions (m x n)

 		Args:
   			heights (list): Water Grid

      		Returns:
			peaks (list): Points where water can flow to both
   		'''	
        	pacific = set()
        	atlantic = set()
        	R, C = len(heights), len(heights[0])

        	for i in range(R):
            		pacific.add((i, 0))
            		atlantic.add((i, C - 1))
        	for j in range(C):
            		pacific.add((0, j))
            		atlantic.add((R - 1, j))

        	dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        	def bfs(starts: set, visited: set):
			'''BFS Through Points

   			Args:
      				starts (list): Starting co-ordinates
	  			visited (list): Visited co-ordinates
      			'''
            		queue = deque(starts)
            		while queue:
                		x, y = queue.popleft()

                		for dx, dy in dirs:
                    			nx, ny = x + dx, y + dy

                    		if (nx >= 0 and nx < R 
				    and ny >= 0 and ny < C 
				    and (nx, ny) not in visited 
				    and heights[nx][ny] >= heights[x][y]):
                        		queue.append((nx, ny))
                        		visited.add((nx, ny))

        	bfs(pacific, pacific)
        	bfs(atlantic, atlantic)

        	return [x for x in pacific if x in atlantic]
        
	def solve(self, board: List[List[str]]) -> None:
		'''Convert Surrounded Regions

  		Space Complexity: O(m * n) -> Grid shape
    		Time Complexity: O(m * n) -> BFS

      		Values: Grid dimensions (m x n)

 		Args:
   			board (list): Grid of Xs and Os
      		'''
		edges = deque()
        	R, C = len(board), len(board[0])
        
        	for i in range(R):
            		if board[i][0] == 'O':
                		edges.append((i, 0))
            		if board[i][C - 1] == 'O':
                		edges.append((i, C - 1))
        	for j in range(C):
            		if board[0][j] == 'O':
                		edges.append((0, j))
            		if board[R - 1][j] == 'O':
                		edges.append((R - 1, j))

        	seen = set()
        	dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
		while edges:
            		x, y = edges.popleft()

            		if (x, y) in seen:
                		continue
            		board[x][y] = 'T'
            		seen.add((x, y))

			for dx, dy in dirs:
                		nx, ny = x + dx, y + dy
                		if (nx >= 0 and nx < R and ny >= 0 and ny < C 
				    and board[nx][ny] == 'O'):
                    			edges.append((nx, ny))

        	for i in range(R):
            		for j in range(C):
                		if board[i][j] == 'T':
                    			board[i][j] = 'O'
                		else:
                    			board[i][j] = 'X'


	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		'''Can Schedule Courses

  		Space Complexity: O(V + E) -> Topological Sort
    		Time Complexity: O(V + E) -> Topological Sort

      		Values: Number of courses (V), Number of prerequisites (E)

		Args:
  			numCourses (int): Number of courses
     			prerequisites (list): Prerequisite mapping

 		Returns:
   			can_schedule (bool): If Course Schedule is Possible
      		'''
        	pre = {i: [] for i in range(numCourses)}
        	for a, b in prerequisites:
            		pre[a].append(b)

        	visited = set()

        	def dfs(cur: int) -> bool:
			'''DFS through course map

   			Args:
      				cur (int): Course index

   			Returns:
      				can_schedule (bool): Consistency of prerequisites
			'''
            		if cur in visited:
                		return False

            		visited.add(cur)
            		for p in pre[cur]:
                		if not dfs(p):
                    			return False
            		visited.remove(cur)
            		
			return True

        	for i in range(numCourses):
            		if not dfs(i):
                		return False
        	return True

	def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
		'''Find order of course schedules

		Space Complexity: O(V + E) -> Topological Sort
    		Time Complexity: O(V + E) -> Topological Sort

      		Values: Number of courses (V), Number of prerequisites (E)

		Args:
  			numCourses (int): Number of courses
     			prerequisites (list): Prerequisite mapping

 		Returns:
   			schedule (list): Course schedule
      		'''
  		pre = {i: [] for i in range(numCourses)}
        	for a, b in prerequisites:
            		pre[a].append(b)

        	schedule = []
        	valid, visited = set(), set()
        
		def dfs(cur) -> bool:
			'''DFS through course map

   			Args:
      				cur (int): Course index

   			Returns:
      				can_schedule (bool): Consistency of prerequisites
			'''
            		if cur in visited:
                		return False
            		if cur in valid:
                		return True
            
            		visited.add(cur)
            		for p in pre[cur]:
                		if not dfs(p):
                    			return False
            		visited.remove(cur)

            		valid.add(cur)
            		schedule.append(cur)

            		return True

        	for i in range(numCourses):
            		if not dfs(i):
                		return []
        	return schedule
        
	def validTree(self, n: int, edges: List[List[int]]) -> bool:
		'''Check if graph is valid tree

  		Space Complexity: O(V + E) -> Topological Sort
    		Time Complexity: O(V + E) -> Topological Sort

      		Values: Number of nodes (V), Number of edges (E)

		Args:
  			n (int): Number of nodes
     			edges(list): Undirected edges

 		Returns:
   			is_tree (bool): If graph is tree
      		'''
        	graph = {i: [] for i in range(n)}
        	for a, b in edges:
            		graph[a].append(b)
            		graph[b].append(a)

        	visited = set()
        	
		def dfs(cur: int, prev: int) -> bool:
			'''DFS through graph

   			Args:
      				cur (int): Current node
	  			prev (int): Previous node

      			Returns:
	 			is_tree (bool): Is valid tree
     			'''
           		if cur in visited:
                		return False
            
            		visited.add(cur)
            		for n in graph[cur]:
                		if n != prev:
                    			if not dfs(n, cur):
                        			return False
            		return True

        	return dfs(0, -1) and len(visited) == n

	def countComponents(self, n: int, edges: List[List[int]]) -> int:
		'''Count Connected Components

		Space Complexity: O(V + E) -> DFS
    		Time Complexity: O(V + E) -> DFS

      		Values: Number of nodes (V), Number of edges (E)

		Args:
  			n (int): Number of nodes
     			edges (list): Edges

 		Returns:
   			cc (int): Number of connected components
      		'''  		
        	graph = {i: [] for i in range(n)}
        	for a, b in edges:
            		graph[a].append(b)
            		graph[b].append(a)

        	cc = 0

        	def dfs(cur: int):
			'''DFS Through Graph

   			Args:
      				cur (int): Current node
	  		'''
            		if cur not in graph:
                		return
            
			nodes = graph[cur]
            		del graph[cur]

            		for n in nodes:
                		dfs(n)

        	while graph:
            		cc += 1
            		dfs(list(graph.keys())[0])

        	return cc


	def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
		'''Find Redundant Connection

		Space Complexity: O(V + E) -> BFS
    		Time Complexity: O(V + E) -> BFS

      		Values: Number of nodes (V), Number of edges (E)

		Args:
     			edges (list): Edges

 		Returns:
   			red (list): Redundant Edge
      		'''
		n = len(edges)
        	indegree = [0] * (n + 1)
        	adj = [[] for _ in range(n + 1)]
        
		for a, b in edges:
            	adj[a].append(b)
            	adj[b].append(a)
            	indegree[a] += 1
            	indegree[b] += 1

        	queue = deque()

        	for i in range(1, n + 1):
            		if indegree[i] == 1:
                		queue.append(i)

        	while queue:
            		node = queue.popleft()
            		indegree[node] -= 1
            		
			for n in adj[node]:
                		indegree[n] -= 1
                		if indegree[n] == 1:
                    			queue.append(n)

        	for a, b in edges[::-1]:
            		if indegree[a] == 2 and indegree[b]:
                		return [a, b]
        
        	return []


	def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
		'''Word Ladder Length

  		Space Complexity: O(n * m): Dictionary
    		Time Complexity: O(n * m): BFS

      		Values: Number of words (n), Length of words (m)

 		Args:
   			beginWord (str): Start word
      			endWord (str): End word
	 		wordList (list): Dictionary

    		Returns:
      			d (int): Length of Word Ladder
	 	'''
        	wild = defaultdict(list)
        	for word in wordList:
            		for i in range(len(word)):
                		star_word = word[:i] + '*' + word[i + 1:]
                		wild[star_word].append(word)

        	seen = set()
        	queue = deque([(beginWord, 1)])

        	while queue:
            		cur, d = queue.popleft()

            		if cur == endWord:
                		return d

            		for i in range(len(cur)):
                		star_word = cur[:i] + '*' + cur[i + 1:]
                		
				if star_word in seen:
                    			continue
                		seen.add(star_word)

                		for next_word in wild[star_word]:
                    			if next_word != cur:
                        			queue.append((next_word, d + 1))
	        return 0
