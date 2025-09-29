// Problem ID: 26
// Title: Remove Duplicates from Sorted Array
// Runtime: 12 ms

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int slow=0,fast=1;
        if (nums.size()==0){
            return 0;
        }
        while(fast<nums.size()){
            if (nums[slow]==nums[fast]){
                fast++;
            }
            else{
                slow++;
                nums[slow]=nums[fast];
                fast++;
            }
        }
        return slow+1;
    }
};