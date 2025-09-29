// Problem ID: 808
// Title: Number of Matching Subsequences
// Runtime: 99 ms

class Solution {
    public int numMatchingSubseq(String s, String[] words) {
        
        Map <Character, Queue<String>> map = new HashMap<>();
        for (int i = 0; i< s.length(); i++){
            char c = s.charAt(i);
            map.putIfAbsent(c, new LinkedList<>());
        }

        for (String word : words){
            char c = word.charAt(0);
            if (map.containsKey(c)){
                map.get(c).add(word);
            }
        }

        int ans = 0;

        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            Queue<String> q = map.get(c);
            int size = q.size();
            for (int j=0;j<size;j++){
                String str = q.poll();
                if (str.length() == 1){
                    ans++;
                }
                else{
                    if(map.containsKey(str.charAt(1))){
                        map.get(str.charAt(1)).add(str.substring(1));
                    }
                }
            } 

        }
        return ans;

    }
}