// Problem ID: 88
// Title: Merge Sorted Array
// Runtime: 4 ms

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i=m+n-1,n1=m-1,n2=n-1,j,temp;
        if (n>0){
            while(n1>=0 && n2>=0){
                if (nums1[n1]>=nums2[n2]){
                    nums1[i]=nums1[n1];
                    n1--;
                    i--;
                }
                else{
                    nums1[i]=nums2[n2];
                    n2--;
                    i--;
                }
            }
            if (n2>=0){
                while(n2>=0){
                    nums1[n2]=nums2[n2];
                    n2--;
                }
            }
        }
    }
};