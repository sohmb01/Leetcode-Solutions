# Problem ID: 1396
# Title: Count Servers that Communicate
# Runtime: 17 ms

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        rows = defaultdict(set)
        cols = defaultdict(set)
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    rows[i].add(j)
                    cols[j].add(i)
        s = set()
        for k,v in rows.items():
            if len(v)>1:
                for c in v:
                    s.add((k,c))
        for k,v in cols.items():
            if len(v)>1:
                for r in v:
                    s.add((r,k))
        return len(s)

