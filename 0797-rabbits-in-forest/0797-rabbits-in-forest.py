class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        res = 0
        rem = 0
        pos = 0
        while pos <len(answers):
            res += answers[pos] + 1
            j = pos
            while j-pos <= answers[pos] and answers[j] == answers[pos]:
                j += 1
                if j >= len(answers):
                    return res
            pos = j
        return res