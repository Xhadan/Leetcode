class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = "" # Store the actual word for easy retrieval

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node):
            # Base Case: Out of bounds, visited, or char not in Trie
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            
            # If we found a word, add to results
            if node.isWord:
                res.add(node.word)
                # Optimization: Don't find the same word twice
                node.isWord = False 
            
            # Explore neighbors
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)
            
            # Backtrack
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
                
        return list(res)