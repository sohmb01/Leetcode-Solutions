/**
 * Leetcode Solution for: 165. Compare Version Numbers
 * Difficulty: Medium
 * URL: https://leetcode.com/problems/compare-version-numbers/submissions/1780388963/
 * Submitted: 2025-09-24T15:20:15.887Z
 */

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1,v2 = version1.split("."),version2.split(".")
        if len(v1) > len(v2):
            return -self.compareVersion(version2,version1)
        v1 += ["0"] * (len(v2)-len(v1))
        for a,b in zip(v1,v2):
            if int(a) > int(b):
                return 1
            elif int(a) < int(b):
                return -1
        return 0