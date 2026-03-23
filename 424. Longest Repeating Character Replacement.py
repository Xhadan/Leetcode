            counts[ord(s[r])-65] += 1
            while (r-l+1) - max(counts) > k:
                counts[ord(s[l])-65] -= 1
                l+=1
            longest = max(longest, r-l+1)
        return longest
