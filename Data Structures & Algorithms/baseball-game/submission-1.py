class Solution:
    def calPoints(self, operations: List[str]) -> int:
        length = len(operations)
        score=[]
        for i in range(length):
            if (operations[i] == "+"):
                score.append(score[-1] + score[-2])
            elif (operations[i] == "C"):
                score.pop()
            elif (operations[i] == "D"):
                score.append(score[-1] * 2)
            else:
                score.append(int(operations[i]))
        finalScore = 0
        print (score)
        for i in range(len(score)):
            finalScore+=score[i]
        return finalScore