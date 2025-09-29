# Problem ID: 1524
# Title: String Matching in an Array
# Runtime: 1 ms

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key = lambda word: len(word))
        n = len(words)
        ans =[]
        for i in range(n):
            for j in range(i+1,n):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break

        return ans