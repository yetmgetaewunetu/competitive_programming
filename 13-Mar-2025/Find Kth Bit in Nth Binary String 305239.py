# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def bitBuilder(self,n,s):
        if n == 0:
            return s
        s.append('1')
        temp = [0]*(len(s)-1)
        for i in range(len(s)-1):
            temp[-(i+1)] = str(int(not int(s[i])))

        s.extend(temp)
        return self.bitBuilder(n-1,s)

    def findKthBit(self, n: int, k: int) -> str:
        bits = self.bitBuilder(n-1,['0'])
        return bits[k-1]