# Problem ID: 1228
# Title: Minimum Cost Tree From Leaf Values
# Runtime: 4 ms

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # 6, 2, 4, 5, 3, 8
        res = 0
        while len(arr)>1:
            idx = arr.index(min(arr))
            if 0 < idx < len(arr)-1:
                res += min(arr[idx-1],arr[idx+1]) * arr[idx]
            else:
                res += arr[1 if idx == 0 else idx-1] * arr[idx]
            arr.pop(idx)
        return res 