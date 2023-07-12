class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        List = []
        for h in range(len(heights)):
            List.append([heights[h], h])
        List.sort()
        answer = []

        for i in List:
            answer.append(names[i[1]])


        my = []
        for i in range(len(answer)):
            my.append(answer.pop())
        return my