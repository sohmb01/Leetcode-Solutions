// Problem ID: 738
// Title: Monotone Increasing Digits
// Runtime: 1 ms

class Solution {
    public int monotoneIncreasingDigits(int n) {
        char[] s = String.valueOf(n).toCharArray();
        int i = 1;
        while (i<s.length && s[i-1] <= s[i]){
            i++;
        }
        while (i>0 && i<s.length && s[i-1]>s[i]){
            s[--i]--;
        }
        for (int j = i+1; j<s.length; j++){
            s[j] = '9';
        }
        return Integer.parseInt(String.valueOf(s));

    }
}