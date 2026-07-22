class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for l in range(len(operations)):
            if operations[l] =="+":
                score.append(score[-1] + score[-2])
            elif operations[l] =="D":
                score.append(score[-1]*2)
            elif operations[l] == "C":
                score.pop()
            else:
                score.append(int(operations[l]))
        
        finalScore = 0
        for num in score:
            finalScore+= num
        
        return finalScore
            