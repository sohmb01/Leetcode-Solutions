// Problem ID: 27
// Title: Remove Element
// Runtime: 4 ms

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if (nums.size()==0){
            return 0;
        }
        int i=0;
        while(i<nums.size()){
            if (nums[i]==val){
                nums.erase(nums.begin()+i);
                continue;
            }
            i++;
        }
        return nums.size();
    }
};