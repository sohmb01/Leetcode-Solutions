# Problem ID: 1006
# Title: Vowel Spellchecker
# Runtime: 39 ms

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def transform(word):
            l = []
            for c in word:
                if c.lower() in "aeiou":
                    l.append("*")
                else:
                    l.append(c.lower())
            return "".join(l)

        words = set(wordlist)
        lower = {}
        vowel = {}
        for word in wordlist:
            lower.setdefault(word.lower(),word)
            vowel.setdefault(transform(word),word)
        
        ans = []
        for query in queries:
            if query in words:
                ans.append(query)
            elif query.lower() in lower:
                ans.append(lower[query.lower()])
            elif transform(query) in vowel:
                ans.append(vowel[transform(query)])
            else:
                ans.append("")
            
        return ans
