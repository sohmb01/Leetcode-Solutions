# Problem ID: 648
# Title: Replace Words
# Runtime: 167 ms

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = sorted([(len(root),root) for root in dictionary ], key = lambda x:x[0])
        
        sentence = sentence.split(" ")
        for i , word  in enumerate(sentence):
            for length, root in dictionary:
                if word[:length] == root:
                    sentence[i] = root
                    break
        return " ".join(sentence)
                