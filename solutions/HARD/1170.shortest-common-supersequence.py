# Problem ID: 1170
# Title: Shortest Common Supersequence 
# Runtime: 536 ms

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # rows, cols = len(str2),len(str1)
        # dp = [["" for _ in range(cols+1)] for _ in range(rows+1)]
        # for i in range(rows):
        #     dp[i][cols] = str2[i:]
        # for j in range(cols):
        #     dp[rows][j] = str1[j:]
        
        # for i in range(rows-1, -1, -1):
        #     for j in range(cols-1, -1, -1):
        #         if str2[i] == str1[j]:
        #             dp[i][j] = str1[j] + dp[i+1][j+1]
        #         else:
        #             if len(dp[i][j+1]) > len(dp[i+1][j]):
        #                 dp[i][j] = str2[i] + dp[i+1][j]
        #             else:
        #                 dp[i][j] = str1[j] + dp[i][j+1]
        # return dp[0][0]

        l1, l2 = len(str1), len(str2)
        prev, curr = [""]* (l1+1), [""]* (l1+1)

        for i in range(l1):
            prev[i] = str1[i:]

        for j in range(l2-1,-1,-1):
            curr[-1] = str2[j:]
            for i in range(l1-1,-1,-1):
                if str1[i] == str2[j]:
                    curr[i] = str1[i] + prev[i+1]
                else:
                    if len(curr[i+1]) > len(prev[i]):
                        curr[i] = str2[j] + prev[i]
                    else:
                        curr[i] = str1[i] + curr[i+1]
            curr, prev = [""]* (l1+1), curr
        return prev[0]





        

        



