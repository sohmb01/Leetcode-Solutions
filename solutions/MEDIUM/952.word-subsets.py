# Problem ID: 952
# Title: Word Subsets
# Runtime: 275 ms

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        uniSets = []
        subSets = defaultdict(int)
        for word in words2:
            d = defaultdict(int)
            for c in word:
                d[c]+=1
                subSets[c] = max(subSets[c],d[c])
        
        for word in words1:
            d = defaultdict(int)
            for c in word:
                d[c]+=1
            isUni = True
            for char, cnt in subSets.items():
                if cnt > d[char]:
                    isUni = False
                    break
            if isUni:
                uniSets.append(word)

        return uniSets
