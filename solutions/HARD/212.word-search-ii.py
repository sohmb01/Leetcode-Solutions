# Problem ID: 212
# Title: Word Search II
# Runtime: 6629 ms

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = ""

    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        ans = set()
        for word in words:
            trie.insert(word)

        def help(curr,i,j,visited):
            if curr.isWord:
                ans.add(curr.isWord)
            if i<0 or j<0 or i>=rows or j>=cols or (i,j) in visited or board[i][j] not in curr.children:
                return 
            visited.add((i,j))
            c = board[i][j]
            help(curr.children[c],i,j+1,visited)
            help(curr.children[c],i+1,j,visited) 
            help(curr.children[c],i-1,j,visited) 
            help(curr.children[c],i,j-1,visited)
            visited.remove((i,j))
        
        visited = set()
        rows, cols = len(board),len(board[0])
        for i in range(rows):
            for j in range(cols):
                
                x = help(trie,i,j,visited)
                if x:
                    ans.append(x)
        return list(ans)