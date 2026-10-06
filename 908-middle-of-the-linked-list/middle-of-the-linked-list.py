# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        f = head
        s = head
        while f is not None and f.next is not None :
            s = s.next
            f = f.next.next

        return s
                            


        