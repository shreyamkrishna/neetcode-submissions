class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        length = len(students) # len(students) = len(sanchwiches)
        q = deque(students)
        unable = length
        for sandwich in sandwiches:
            count = 0
            while (count < unable and sandwich != q[0]):
                count +=1
                cur = q.popleft()
                q.append(cur)
            
            if q[0] == sandwich:
                q.popleft()
                unable -=1
            else:
                break
        return unable
        