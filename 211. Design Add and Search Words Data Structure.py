class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        """
        Standard Trie Insertion
        O(L) Time
        """
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr["."] = "."  # End of word marker

    def search(self, word: str) -> bool:
        """
        DFS Search with Wildcard support
        O(L) for normal words, O(26^L) for worst-case wildcards
        """
        def dfs(index, curr_dict):
            curr = curr_dict
            
            for i in range(index, len(word)):
                char = word[i]
                
                if char == ".":
                    # Wildcard: Try every possible child at this level
                    for child in curr:
                        if child != "." and dfs(i + 1, curr[child]):
                            return True
                    return False
                else:
                    # Standard letter check
                    if char not in curr:
                        return False
                    curr = curr[char]
            
            return "." in curr

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)