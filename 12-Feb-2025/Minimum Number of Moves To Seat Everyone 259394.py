# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        i, n = 0, len(seats)
        res = 0
        while i < n:
            res+= abs(seats[i]-students[i])
            i += 1
        return res