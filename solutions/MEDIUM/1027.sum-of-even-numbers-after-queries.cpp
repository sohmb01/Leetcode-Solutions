// Problem ID: 1027
// Title: Sum of Even Numbers After Queries
// Runtime: 196 ms

class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& A, vector<vector<int>>& queries) {
        vector<int> ans;
        int q=queries.size(),i,sum=0,temp,val;
        for(i=0;i<A.size();i++){
            if(A[i]%2==0){
                sum+=A[i];
            }  
        }
        for(i=0;i<q;i++){
            temp=A[queries[i][1]];
            val=queries[i][0];
            A[queries[i][1]]=A[queries[i][1]]+val;
            if (abs(A[queries[i][1]])%2==0){
                if(temp%2==0){
                    sum+=A[queries[i][1]];
                    sum-=temp;
                }
                else{
                    sum+=A[queries[i][1]];
                }
            }
            else{
                if(temp%2==0){
                    sum-=temp;
                }
                
            }
            ans.push_back(sum);
        }
        return ans;
        
        
        
    }
};