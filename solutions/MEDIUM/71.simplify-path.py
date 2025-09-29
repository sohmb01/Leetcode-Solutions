# Problem ID: 71
# Title: Simplify Path
# Runtime: 3 ms

class Solution:
    def simplifyPath(self, path: str) -> str:

        sp = [x for x in path.split("/")]
        stk = []
        print(sp)
        for p in sp:
            if not p or p==".":
                continue
            if stk and p == "..":
                stk.pop()
            elif p!="..":
                stk.append(p)
        return "/"+"/".join(stk)


