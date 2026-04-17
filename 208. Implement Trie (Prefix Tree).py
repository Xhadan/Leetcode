class Trie:

    def __init__(self):
        # The root is an empty dictionary
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        Complexity: O(L) time, O(L) space
        """
        curr = self.root
        for char in word:
            # If the character is not in the current level, add a new dictionary
            if char not in curr:
                curr[char] = {}
            # Move into the next nested dictionary
            curr = curr[char]
        # Mark the end of the word with a special character
        curr["."] = "."

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        Complexity: O(L) time
        """
        curr = self.root
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
        # It's only a full word if the terminator exists
        return "." in curr

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        Complexity: O(L) time
        """
        curr = self.root
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        # If we successfully traversed all characters in the prefix, return True
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)