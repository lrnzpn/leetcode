"""
https://leetcode.com/problems/running-sum-of-1d-array/
"""

# first implem
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        
        result = []
        for i in nums:
            result.append(sum(nums[:i:]))
        return result
    
# array approach
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        result = [nums[0]]
        for i in range(1, len(nums)):
            result.append(nums[i] + result[i-1])
        return result
    
# variable for sum
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        result = []
        s = 0
        for i in nums:
            s += i
            result.append(s)
        return result
    
# inplace solution
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums