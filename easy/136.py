"""
https://leetcode.com/problems/single-number/
"""

from typing import List

# first solution, brute force way
# memory beats 100% but is super duper slow O(n^2)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for x in nums:
            if x not in counter:
                counter[x]=nums.count(x)
        return [x for x in counter if counter[x]==min(counter.values())][0]