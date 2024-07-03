package easy;
/**
 * https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
 */

// first solution, brute force way
class Solution {
  public int findNumbers(int[] nums) {
      int count = 0;
      for(int i = 0;i < nums.length; i++) {
          int digits = 0;
          double num = nums[i];
          while(num >= 1) {
              // hint: keep dividing number by 10
              num = num / 10;
              digits = digits + 1;
          }
          if(digits % 2 == 0) {
              count = count + 1;
          }
      }
      return count;
  }
}

// cleaner way, removing the other variables i used
class Solution2 {
  public int findNumbers(int[] nums) {
      int count = 0;
      for(int i = 0;i < nums.length; i++) {
          int digits = 0;
          while(nums[i] != 0) {
              digits++;
              nums[i] = nums[i] / 10;
              
          }
          if(digits % 2 == 0) {
            count++;
          }
      }
      return count;
  }
}