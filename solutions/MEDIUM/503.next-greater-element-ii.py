# Problem ID: 503
# Title: Next Greater Element II
# Runtime: 13 ms

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mxIdx = nums.index(max(nums))
        mxEle = nums[mxIdx]
        l = [-1]*n
        st = [nums[mxIdx]]
        for i in range(mxIdx-1,-1,-1):
            if nums[i] == mxEle:
                l[i] = -1
                st.append(nums[i])
                continue
            if st[-1]<=nums[i]:
                while st[-1]<=nums[i]:
                    st.pop()
            l[i] = st[-1]
            st.append(nums[i])
        
        for i in range(n-1,mxIdx,-1):
            if nums[i] == mxEle:
                l[i] = -1
                st.append(nums[i])
                continue
            if st[-1]<=nums[i]:
                while st[-1]<=nums[i]:
                    st.pop()
            l[i] = st[-1]
            st.append(nums[i])
        return l

