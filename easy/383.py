"""
https://leetcode.com/problems/ransom-note/
"""
# first implem using hashmap, the best way to do it
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for m in magazine: 
            # hashmap.get(m, 0) sets default to value to 0, then we add 1
            hashmap[m] = hashmap.get(m, 0) + 1
        for r in ransomNote:
            # here, we get hashmap value and return 0 if no value
            curr = hashmap.get(r, 0)
            if curr == 0:
                return False
            hashmap[r] = curr - 1
        return True