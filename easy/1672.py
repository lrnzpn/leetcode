""" 
https://leetcode.com/problems/richest-customer-wealth/
"""
from typing import List

# first solution: set default max then change max when to new when sum is bigger
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            s = sum(accounts[i])
            if s > max_wealth:
                max_wealth = s
                
        return max_wealth

# same approach but using max()
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            current_wealth = sum(account)
            max_wealth = max(max_wealth, current_wealth)
        return max_wealth