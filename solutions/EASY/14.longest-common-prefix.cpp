// Problem ID: 14
// Title: Longest Common Prefix
// Runtime: 4 ms

class Solution {
public:
    string getPrefix(string a,string b){
        int i=0,na=min(a.size(),b.size());
        string s;
        while(i<na && a[i]==b[i]){
            s+=a[i];
            i++;
        }
        return s;
    }
    string longestCommonPrefix(vector<string>& strs) {
        int i,n=strs.size();
        if (n==0){
            return "";
        }
        string prefix=strs[0];
        for(i=1;i<n;i++){
            prefix=getPrefix(prefix,strs[i]);
            if (prefix==""){
                break;
            }
        }
        return prefix;
        
        
    }
};