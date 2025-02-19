# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n= 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        mid = ceil(n/2)
        i = 1
        memo = {}
        cur = head
        for i in range(1,mid+1):
            memo[i]  = cur.val
            cur = cur.next
        i += 1
        j = 1
        if n % 2:
            j = 2
        while i <=n:
            # print(memo,i,i-j)
            if memo[i - j] != cur.val:
                return False
            cur = cur.next
            i += 1
            j += 2
        return True