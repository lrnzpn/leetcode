package easy;

/**
 * https://leetcode.com/problems/duplicate-zeros/
 */

// first solution using 2 loops
// first loop to iterate forward and check for zeros
// second loop to shift array to the right
// lastly, set new values (to zero) then skip (iterate)
class Solution {
  public void duplicateZeros(int[] arr) {
    for(int i = 0; i < arr.length; i++) {
      if(arr[i] == 0 && i+1 < arr.length) {
          for(int j = arr.length-1; j > i+1; j--) {
              arr[j] = arr[j-1];
          }
          arr[i+1] = 0;
          i++;
      }
    } 
  }
}