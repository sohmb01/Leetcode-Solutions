# Problem ID: 49
# Title: Group Anagrams
# Runtime: 92 ms

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        ans = []
        for s in strs:
            sortedString = str(sorted(s))
            if not sortedString in mp:
                mp[sortedString] = []
            mp[sortedString].append(s)
        
        for value in mp.values():
            ans.append(value)

        return sorted(ans,key= len)