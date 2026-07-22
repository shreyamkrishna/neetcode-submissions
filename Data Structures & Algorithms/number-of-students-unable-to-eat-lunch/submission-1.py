class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones = sum (students)
        zeros = len(students) - ones

        for s in sandwiches: 
            if s==0 and zeros>0:
                zeros -=1
            elif s==1 and ones>0:
                ones-=1
            else:
                break
        
        return ones+zeros