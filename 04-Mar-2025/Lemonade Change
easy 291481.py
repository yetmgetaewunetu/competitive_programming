# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five >0:
                    ten += 1
                    five -=1
                else:
                    return False
            else:
                if 5 * five + ten * 10 >= 15 and five:
                    if ten and five:
                        ten -=1
                        five -=1
                    else:
                        five -= 3
                else:
                    return False
        return True