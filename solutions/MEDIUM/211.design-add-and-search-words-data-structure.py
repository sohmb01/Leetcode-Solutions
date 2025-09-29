# Problem ID: 211
# Title: Design Add and Search Words Data Structure
# Runtime: 798 ms

class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["isWord"] = True

    def search(self, word: str) -> bool:
        root = self.root
        def help(curr, s):
            if type(curr) == type(True):
                return False
            if not s:
                return "isWord" in curr
            if s[0] not in curr:
                if s[0] == ".":
                    ans = False
                    for c in curr:
                        ans = ans or help(curr[c],s[1:])
                else:
                    ans = False
                return ans
            else:
                curr = curr[s[0]]
                return help(curr,s[1:])
        return help(root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)