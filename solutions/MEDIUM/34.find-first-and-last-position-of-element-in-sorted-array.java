// Problem ID: 34
// Title: Find First and Last Position of Element in Sorted Array
// Runtime: 0 ms

class Solution {
    public int[] searchRange(int[] nums, int target) {
        
        int [] result = {-1,-1};
        result[0] = binarySearch(nums,target, true);
        result[1] = binarySearch(nums,target, false);
        return result;

    }

    private int binarySearch(int[] nums, int target, boolean isSearchingLeft){
        
        int idx = -1;
        int left = 0;
        int right = nums.length -1;
        int mid = left + (right-left)/2 ; 
        while (left <= right){
            mid = left + (right-left)/2 ; 
            if (target < nums[mid]){
                right = mid-1;
            }
            else if (target > nums[mid]){
                left = mid+1;
            }
            else{
                idx = mid;
                if (isSearchingLeft){
                    right = mid-1;
                }
                else{
                    left = mid+1;
                }
            }
        }
        return idx;
    }
}