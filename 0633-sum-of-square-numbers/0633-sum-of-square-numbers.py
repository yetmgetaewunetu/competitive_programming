class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        a = 0
        while a * a <= c:
            target = sqrt(c - a*a)
            tar= int(target)
            print(target,tar)
            if target == tar:
                return True
            a += 1
        return False
        