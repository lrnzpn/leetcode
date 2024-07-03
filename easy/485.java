package easy;
/**
 * https://leetcode.com/problems/max-consecutive-ones/
 */

class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int counter = 0;
        int max = 0;
        for(int i = 0;i < nums.length;i++) {
            if(nums[i] == 1) {
                counter = counter + 1;
                max = Math.max(max, counter);
            } else {
                counter = 0;
            }
        }
        return max;
    }
}