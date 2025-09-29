# Problem ID: 3569
# Title: Count of Substrings Containing Every Vowel and K Consonants II
# Runtime: 1917 ms

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)

        def atLeastK(k):
            l,r = 0,0
            consonants = 0
            vowels = set(["a","e","i","o","u"])
            freq = defaultdict(int)
            cnt,l = 0,0
            for r in range(n):
                if word[r] in vowels:
                    freq[word[r]]+=1
                else:
                    consonants+=1
                while len(freq) == 5 and consonants>=k:
                    cnt+= n-r
                    if word[l] in vowels:
                        freq[word[l]]-=1
                    else:
                        consonants-=1
                    if freq[word[l]] == 0:
                        freq.pop(word[l])
                    l+=1
            return cnt
        return atLeastK(k)-atLeastK(k+1)
            
