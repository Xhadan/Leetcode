from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 1. We use a defaultdict of lists
        res = defaultdict(list)

        for s in strs:
            # 2. Create the 26-zero array
            count = [0] * 26

            for c in s:
                # 3. Base + Offset logic
                count[ord(c) - ord("a")] += 1

            # 4. Use the immutable tuple as the key
            res[tuple(count)].append(s)

        # 5. Return the grouped lists
        return list(res.values())