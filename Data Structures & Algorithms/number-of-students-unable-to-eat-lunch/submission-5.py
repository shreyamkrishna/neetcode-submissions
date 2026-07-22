class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones = 0
        zeros = 0
        for student in students:
            if student:
                ones+=1
            else:
                zeros+=1
        
        for sandwich in sandwiches:
            if sandwich and ones:
                ones-=1
            elif sandwich == 0 and zeros:
                zeros-=1
            else:
                break
        
        return zeros+ones