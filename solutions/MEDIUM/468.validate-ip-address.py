# Problem ID: 468
# Title: Validate IP Address
# Runtime: 0 ms

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def isIPv4(s):
            l = s.split(".")
            if len(l) != 4:
                return False
            for x in l:
                if (not x.isnumeric()) or int(x)<0 or int(x)>255 or (len(x)>1 and x[0]=="0"):
                    return False
            return True 

        def isIPv6(s):
            l = s.split(":")
            if len(l) != 8:
                return False
            for x in l:
                if len(x)== 0 or len(x) > 4:
                    return False
                for c in x:
                    print(c)
                    if not (c.isdigit() or c.lower() in ['a','b','c','d','e','f']):
                        return False
            return True
        
        if isIPv4(queryIP):
            return "IPv4"
        if isIPv6(queryIP):
            return "IPv6"

        return "Neither"
        