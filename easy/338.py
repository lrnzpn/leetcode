"""
https://leetcode.com/problems/counting-bits/
"""

from typing import List

# memory efficient but really slow due to implem
class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for x in range(0,n+1):
            out.append(bin(x)[2:].count('1'))

        return out