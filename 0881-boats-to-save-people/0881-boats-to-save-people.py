#people = [3,5,3,4]
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left,right = 0, len(people) - 1
        count = 0
        while left <= right:
            if people[left] + people[right] > limit:
                right -= 1
                count += 1
                continue
            else:
                left += 1
                right -= 1
                count += 1
        return count