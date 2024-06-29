"""
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
"""

# recursion way, first solution i could think of
# apparently another solution is to use bitwise (& and >> operators) but i am not familiar
class Solution:
    def numberOfSteps(self, num: int, counter: int = 0) -> int:
        if num == 0:
            return counter

        if num % 2 == 0:
            return self.numberOfSteps(num / 2, counter + 1)
        else:
            return self.numberOfSteps(num - 1, counter + 1)