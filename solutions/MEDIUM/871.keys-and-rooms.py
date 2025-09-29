# Problem ID: 871
# Title: Keys and Rooms
# Runtime: 5 ms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        adj = defaultdict(list)
        for room,keys in enumerate(rooms):
            for key in keys:
                adj[room].append(key)
        
        visit = [False]*n
        cnt = [0]
        def dfs(node):
            if visit[node]:
                return
            visit[node]=True
            cnt[0]+=1
            for nei in adj[node]:
                if not visit[nei]:
                    dfs(nei)
        
        dfs(0)
        return cnt[0]==n