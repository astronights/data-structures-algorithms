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
        
