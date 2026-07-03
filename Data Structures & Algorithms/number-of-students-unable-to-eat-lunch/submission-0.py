class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        count_zero = 0
        count_one = 0
        for student in students:
            if student == 0:
                count_zero +=1

            else:
                count_one +=1

        for sandwich in sandwiches:
            if sandwich == 0:
                if count_zero == 0:
                    break
                count_zero -=1
            else:
                if count_one == 0:
                    break
                count_one -=1
                
        return count_zero + count_one


        