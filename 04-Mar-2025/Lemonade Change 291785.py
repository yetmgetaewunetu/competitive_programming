# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif five >0 and bill == 10:
                ten += 1
                five -=1
            else:
                if ten and five:
                    ten -=1
                    five -=1
                elif five >=3:
                    five -= 3
                else:
                    return False
        return True