class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        List = []
        for i in range(len(score)):
            List.append([score[i][k], i])
        List.sort(reverse= True)
        answer = []
        for i in range(len(List)):
            answer.append(score[List[i][1]])
        return answer