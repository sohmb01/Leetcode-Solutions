# Problem ID: 1160
# Title: Letter Tile Possibilities
# Runtime: 43 ms

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = [0]*26
        for tile in tiles:
            freq[ord(tile)-ord('A')]+=1
        def dfs(freq):
            s = 0
            for i in range(26):
                if not freq[i]:
                    continue
                freq[i]-=1
                s += dfs(freq)+1
                freq[i]+=1
            return s
        return dfs(freq)
