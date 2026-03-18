class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # While we have a duplicate, crawl the left pointer forward
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            # Add the new character and update result
            w = (r - l) + 1 
            res = max(res, w)
            char_set.add(s[r])
            
        return res