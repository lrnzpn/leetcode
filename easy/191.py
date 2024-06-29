"""
https://leetcode.com/problems/number-of-1-bits/
"""

# memory efficient but is slower compared to other solutions
# i think this is due to using builtin functions
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')