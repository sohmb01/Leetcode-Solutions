// Problem ID: 442
// Title: Find All Duplicates in an Array
// Runtime: 116 ms

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector <int > ans;
        int i,n=nums.size()+1,index;
        for (i=0;i<nums.size();i++){
            index=(nums[i]-1)%n;
            nums[index]=nums[index]+n;
        }
        for (i=0;i<n-1;i++){
            if (nums[i]/n >1){
                ans.push_back(i+1);
            }
        }
        return ans;
    }
};