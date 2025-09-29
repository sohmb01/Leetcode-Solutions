# Problem ID: 676
# Title: Implement Magic Dictionary
# Runtime: 67 ms

class MagicDictionary:

    def __init__(self):
        self.mp = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.mp[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        for word in self.mp[len(searchWord)]:
            cnt = 0
            for a,b in zip(word,searchWord):
                if a != b:
                    cnt+=1
            if cnt == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)