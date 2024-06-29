"""
https://leetcode.com/problems/two-sum/
"""
from typing import List

# infamous two sum problem
# hashmap way is the most optimal way
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if target-nums[i] in hashmap:
                return [hashmap[target-nums[i]], i]
            else:
                hashmap[nums[i]] = i