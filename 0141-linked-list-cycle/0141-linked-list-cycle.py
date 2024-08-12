class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next is None:
            return False
        s = head
        f = head.next
        while f is not None and f.next is not None:
            if f == s or f.next == s:
                return True
            s = s.next
            f = f.next.next
        return False