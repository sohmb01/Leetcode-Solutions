# Problem ID: 3872
# Title: Find Most Frequent Vowel and Consonant
# Runtime: 7 ms

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set(["a","e","i","o","u"])
        vowelCount, consonantCount = 0,0
        freq = defaultdict(int)
        for c in s:
            freq[c]+=1
            if c in vowels:
                vowelCount = max(vowelCount,freq[c])
            else:
                consonantCount = max(consonantCount,freq[c])
                
        return vowelCount + consonantCount