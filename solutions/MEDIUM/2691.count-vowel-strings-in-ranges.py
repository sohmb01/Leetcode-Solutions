# Problem ID: 2691
# Title: Count Vowel Strings in Ranges
# Runtime: 16 ms

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = {'a','e','i','o','u'}
        prefix = [0]
        last = 0
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                prefix.append(last + 1)
            else:
                prefix.append(last)
            last = prefix[-1]
        ans = []
        for query in queries:
            l,r = query[0],query[1]
            ans.append(prefix[r+1]-prefix[l])
        return ans
