class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid_index = len(s)//2
        last_index = len(s) -1
        for i in range(mid_index):
            s[i], s[last_index - i] = s[last_index - i], s[i]
            