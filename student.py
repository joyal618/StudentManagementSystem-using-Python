class Student:

    def __init__(self, student_rollno, student_class, student_name, student_mark):
        self.student_rollno = student_rollno
        self.student_class = student_class
        self.student_name = student_name
        self.student_mark = student_mark

    def get_details(self):
        return (self.student_rollno,self.student_class,self.student_name,self.student_mark)


