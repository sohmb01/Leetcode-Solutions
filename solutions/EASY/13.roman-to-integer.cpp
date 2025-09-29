// Problem ID: 13
// Title: Roman to Integer
// Runtime: 24 ms

class Solution {
public:
    int romanToInt(string s) {
        int i,num=0,curr,next;
        map<char,int> values;
        values['I']=1;
        values['V']=5;
        values['X']=10;
        values['L']=50;
        values['C']=100;
        values['D']=500;
        values['M']=1000;
        if (s.size()==1){
            return values.find(s[0])->second;
        }
        map<char,int > :: iterator it;
        for (i=0;i<s.size()-1;i++){
            it=values.find(s[i]);
            curr=it->second;
            it=values.find(s[i+1]);
            next=it->second;
            if (curr>=next){
                num+=curr;
            }
            else{
                num-=curr;
            }
        }
        num+=next;
        return num;
    }
};