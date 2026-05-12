    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def addTwoNumbers(self, l1, l2):
            carry = 0
            head = ListNode(0)
            cur = head
            while l1 or l2 or carry:
                x = l1.val if l1 else 0
                y = l2.val if l2 else 0
                s = x + y + carry
                carry = s // 10
                cur.next = ListNode(s % 10)
                cur = cur.next
                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next
            return head.next
            """
            :type l1: Optional[ListNode]
            :type l2: Optional[ListNod  e]
            :rtype: Optional[ListNode]
            """
        