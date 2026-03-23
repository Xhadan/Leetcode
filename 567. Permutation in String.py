class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: 
            return False
        
        # 1. Initialize frequency arrays for s1 and s2's first window
        s1_counts = [0] * 26
        s2_counts = [0] * 26
        
        for i in range(n1):
            s1_counts[ord(s1[i]) - 97] += 1
            s2_counts[ord(s2[i]) - 97] += 1
            
        if s1_counts == s2_counts: return True
        
        # 2. Slide the window through the rest of s2
        for i in range(n1, n2):
            # Add the character coming into the window
            s2_counts[ord(s2[i]) - 97] += 1
            # Remove the character leaving the window (i - n1)
            s2_counts[ord(s2[i - n1]) - 97] -= 1
            
            if s1_counts == s2_counts:
                return True
                
        return False