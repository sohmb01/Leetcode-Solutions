// Problem ID: 12
// Title: Integer to Roman
// Runtime: 12 ms

class Solution {
public:
    string intToRoman(int num) {
        vector<int> values={1000,900,500,400,100,90,50,40,10,9,5,4,1};
        vector<string> roman_digits={"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        string s;
        int i=0,div;
        while(num>0){
            if (values[i]<=num){
                div=num/values[i];
                while(div--){
                    s.append(roman_digits[i]);
                }
                num=num % values[i];
            }
            i++;
            
        }
        return s;
    }
};