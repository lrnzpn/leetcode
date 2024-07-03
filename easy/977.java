package easy;

/**
 * https://leetcode.com/problems/squares-of-a-sorted-array/
 */

import java.util.Arrays;

// first solution, package dependent using sort
class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] squares = new int[nums.length];
        for(int i = 0;i < nums.length;i++) {
            squares[i] = nums[i] * nums[i];
        }
        Arrays.sort(squares);
        return squares;
    }
}

// a better solution would be to do it using 2 pointers
// from https://leetcode.com/problems/squares-of-a-sorted-array/solutions/4810295/java-two-pointer-one-pass-explained
class Solution2 {
  public int[] sortedSquares(int[] nums) {
      int n = nums.length, si=0, ei = n-1, i=n-1;
      int[] ans = new int[n];
      while(si <= ei){
          // compare squares of start index and end index
          // then add to array depending on result of comparison
          if(nums[si]*nums[si] < nums[ei]*nums[ei]){
              ans[i--] = nums[ei]*nums[ei];
              ei--;
          }else{
              ans[i--] = nums[si]*nums[si];
              si++;
          }
      }
      return ans;

  }
}