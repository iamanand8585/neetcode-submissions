# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None or head.next.next is None:
            return
        else:
            # finding middle node
            fast = head
            slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            # dividind LinkedList in 2 half
            first = head
            second = slow.next
            slow.next = None

            # reversing second half
            before = None
            temp = second
            after = temp.next
            while temp:
                after = temp.next
                temp.next = before
                before = temp
                temp = after
            second = before
        
            while second:
                temp1, temp2 = first.next, second.next
                first.next = second
                second.next = temp1
                first, second = temp1, temp2


            

        

