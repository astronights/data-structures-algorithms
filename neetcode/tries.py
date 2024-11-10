# Tries Solutions

class TrieNode:
        def __init__(self):
                '''Trie Node'''
                self.nodes = {}
                self.isWord = False

class PrefixTree:

        def __init__(self):
                '''Create a Prefix Trie

                Space Complexity: O(t) -> Number of nodes
                '''
                self.trie = TrieNode()

        def insert(self, word: str) -> None:
                '''Insert Word in Trie

                Time Complexity: O(n) -> Length of word

                Args:
                        word (str): Iterable to insert
                '''
                path = self.trie
        
                for c in word:
                        if c not in path.nodes:
                                path.nodes[c] = TrieNode()
                        path = path.nodes[c]
                path.isWord = True


        def search(self, word: str) -> bool:
                '''Search for word in Trie

                Time Complexity: O(n) -> Length of word

                Args:
                        word (str): Iterable to search

                Returns:
                        isWord (bool): If valid word exists
                '''
                path = self.trie
        
                for c in word:
                        if c not in path.nodes:
                                return False
                        path = path.nodes[c]
                return path.isWord

        def startsWith(self, prefix: str) -> bool:
                '''Check if Prefix exists

                Time Complexity: O(n) -> Length of prefix
                
                Args:
                        prefix (str): Iterable to search

                Returns:
                        is_prefix (bool): If valid word exists
                '''
                path = self.trie
                
                for c in prefix:
                        if c not in path.nodes:
                                return False
                        path = path.nodes[c]
                return True
        

class WordDictionary:

        def __init__(self):
                '''Word Search Dictionary with wildcard

                Space Complexity: O(t) -> Number of nodes
                '''
                self.trie = TrieNode()

        def addWord(self, word: str) -> None:
                '''Add Word in Trie

                Time Complexity: O(n) -> Length of word

                Args:
                        word (str): Iterable to insert
                '''
                path = self.trie
                
                for c in word:
                        if c not in path.nodes:
                                path.nodes[c] = TrieNode()
                        path = path.nodes[c]
                path.isWord = True

        def search(self, word: str) -> bool:
                '''Search for word with wildcard

                Time Complexity: O(26^n) -> DFS

                Args:
                        word (str): Iterable to search

                Returns:
                        is_word (bool): If word exists
                '''

                def dfs(i: int, path: TrieNode) -> bool:
                        '''DFS through Trie

                        Args:
                                i (int): Index
                                path (TrieNode): Current path

                        Returns:
                                is_word (bool): If word exists
                        '''
                        nodes = path.nodes
                        if i == len(word):
                                # Final character
                                return path.isWord
                        if word[i] != '.':
                                # Check for a-z characters
                                if word[i] in nodes:
                                    return dfs(i + 1, nodes[word[i]])
                                else:
                                    return False
                        else:
                                # Check for wildcard . characters
                                if len(path.nodes) > 0:
                                    return any((dfs(i + 1, nxt) for nxt in nodes.values()))
                                else:
                                    return False
                return dfs(0, self.trie)

class Solution:
        # Solution Functions

        def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
                '''Find all words in grid

                Space Complexity: O(m * n + s) -> Seen Grid + Trie
                Time Complexity: O(m * n * max(s)) -> DFS for each cell

                Values: Grid Dimensions (m, n), Word Lengths (s)

                Args:
                        board (list): Word Grid
                        words (list): Iterable of words

                Returns:
                        out (list): Words found
                '''
                R, C = len(board), len(board[0])
                trie = PrefixTree()
        
                out, seen = set(), set()
                
                for word in words:
                        trie.insert(word)

                def dfs(i: int, j: int, cur: str, path: TrieNode):
                        '''DFS Through Grid

                        Args:
                                i (int): Row index
                                j (int): Column index
                                cur (str): Word so far
                                path (TrieNode): Trie Node
                        '''
                        char = board[i][j]
                        
                        if (i < 0 or i == R 
                            or j < 0 or j == C 
                            or (i, j) in seen 
                            or char not in path.nodes):
                                return

                        nxt_node = path.nodes[char]
                        nxt_word = cur + char

                        if nxt_node.isWord:
                                out.add(nxt_word)

                        seen.add((i, j))

                        dfs(i + 1, j, nxt_word, nxt_node)
                        dfs(i - 1, j, nxt_word, nxt_node)
                        dfs(i, j + 1, nxt_word, nxt_node)
                        dfs(i, j - 1, nxt_word, nxt_node)

                        seen.remove((i, j))

                for r in range(R):
                        for c in range(C):
                                dfs(r, c, '', trie.trie)
        
                return list(out)
