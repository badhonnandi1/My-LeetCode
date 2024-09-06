# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        solo = []
        temp = head
        while temp:
            solo.append(temp.val)
            temp = temp.next
        
        final = []
        nums_set = set(nums)  
        for i in solo:
            if i not in nums_set:
                final.append(i)
        
        gghead = ListNode(final[0])
        head = gghead
        for i in range(1,len(final)):
            node = ListNode(final[i])
            head.next = node
            head = node
        return gghead
            

#not a good solution I know
#will try to improve the next one.