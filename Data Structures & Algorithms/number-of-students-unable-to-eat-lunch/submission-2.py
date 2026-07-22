class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        l = len(students)
        unable = l
        for sandwich in sandwiches:
            i=0
            while i < l and sandwich != students[0]:
                popped = students[0]
                students = students[1:]
                students.append(popped)
                i+=1 
            
            if students[0] == sandwich:
                students = students[1:]
                unable -=1
            else:
                break
        return unable