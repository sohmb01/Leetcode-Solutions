# Problem ID: 143
# Title: Reorder List
# Runtime: 62 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cnt = 0
        temp = head
        while temp:
            cnt+=1
            temp = temp.next
        
        if cnt<3:
            return head
        cnt = cnt//2 + cnt%2
        i = 1
        temp = head
        while i<cnt:
            i+=1
            temp = temp.next

        head2= temp.next
        temp.next = None

        #reverse the second half of the ll
        temp = head2.next
        head2.next = None
        while temp:
            k = temp.next
            temp.next = head2
            head2 = temp
            temp = k

        temp = head2
        
        while temp:
            print(temp.val)
            temp = temp.next
        
        for i in range(cnt):
            temp = head.next
            head.next = head2
            if not head2:
                break
            head2 = head2.next
            head = head.next
            head.next = temp
            head = head.next
        
            
        
