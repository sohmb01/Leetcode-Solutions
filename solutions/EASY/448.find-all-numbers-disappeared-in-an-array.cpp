// Problem ID: 448
// Title: Find All Numbers Disappeared in an Array
// Runtime: 104 ms

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int i;
        vector <int > ans;
        int n=nums.size()+1;
        for (i=0;i<n-1;i++){
            nums[(nums[i]%n)-1]=nums[(nums[i]%n)-1]+n;
        }
        for (i=0;i<n-1;i++){
            if (nums[i]<n){
                ans.push_back(i+1);    
            }
        }
        return ans;
    }
};