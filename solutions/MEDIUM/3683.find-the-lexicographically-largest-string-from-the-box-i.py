# Problem ID: 3683
# Title: Find the Lexicographically Largest String From the Box I
# Runtime: 404 ms

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        
        def largerLex(a,b):
            for i in range(min(len(a),len(b))):
                if a[i]==b[i]:
                    continue
                elif ord(a[i])>ord(b[i]):
                    return a
                else:
                    return b
            return a if len(a)>len(b) else b

        if numFriends == 1:
            return word

        n = len(word)
        limit = n - numFriends + 1
        indices = [[] for _ in range(26)]
        
        for i,c in enumerate(word):
            indices[ord(c)-ord('a')].append(i)
        
        res = "a"
        for i in range(25,-1,-1):
            if indices[i]:
                for idx in reversed(indices[i]):
                    start = idx
                    end = min(start+limit,n)
                    res = largerLex(word[start:end],res)
                return res


        
        