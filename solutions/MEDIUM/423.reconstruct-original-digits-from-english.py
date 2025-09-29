# Problem ID: 423
# Title: Reconstruct Original Digits from English
# Runtime: 19 ms

class Solution:
    def originalDigits(self, s: str) -> str:
        digits = ["zero", "one", "two","three","four","five","six","seven","eight","nine"]
        uniqueKeys = ["z", "on" , "w", "rh","u", "fv","x","vs","g", "en"]
        l = []
        freq = Counter(s)
        for i in range(10):
            digit, key = digits[i],uniqueKeys[i]
            if len(key) == 1:
                f = freq[key]
                l += [i] * f
                for c in digit:
                    freq[c] -= f
        for i in range(10):
            digit, key = digits[i],uniqueKeys[i]
            if len(key) == 1:
                continue
            f = freq[key[0]]
            l += [i]*f
            for c in digit:
                freq[c] -= f
        
        return "".join([str(x) for x in sorted(l)])
            


            