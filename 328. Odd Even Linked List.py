class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        evenHead = head.next

        while even != None and even.next != None:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = evenHead

        return head
