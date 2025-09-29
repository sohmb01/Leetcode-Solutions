# Problem ID: 79
# Title: Word Search
# Runtime: 4927 ms

class Solution:
    def exist(self, b: List[List[str]], word: str) -> bool:
        st = set()
        def bfs(i,j,s,board):
            if not s:
                return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j] != s[0] or ((i,j) in st):
                return False
            st.add((i,j))
            result =  bfs(i-1,j,s[1:],board) or bfs(i+1,j,s[1:],board) or bfs(i,j-1,s[1:],board) or bfs(i,j+1,s[1:],board)
            st.remove((i,j))
            return result
                            
        
        for i in range(len(b)):
            for j in range(len(b[0])):
                if bfs(i,j,word,b):
                    return True
        return False
            