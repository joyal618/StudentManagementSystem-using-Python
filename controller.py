from student import Student

class Controller:
    def __init__(self):
        self.object_list=list()
    

    def add_student(self):
        temp_student_rollno=input("Enter RollNo of the student: ")
        temp_student_class=input("Enter Class of the student: ")
        temp_student_name=input("Enter Name of the student: ")
        temp_student_mark=int(input("Enter Mark of the student: "))
        object_name = Student(temp_student_rollno,temp_student_class,temp_student_name,temp_student_mark)
        for i in self.object_list:
           if temp_student_class in i.student_class:
               if temp_student_rollno == i.student_rollno:
                    print("\nStudent already exist!!")
                    return None
        self.object_list.append(object_name)
        print("\nStudent Details Added!!")
        self.object_list.sort(key=lambda x: x.student_mark,reverse=True)
       

    def display_student(self):
        print("\n~~ List of Students ~~\nRollNo\tClass\tName\tMark")
        for i in self.object_list:
            for j in (i.get_details()):
                print(j, end ="\t")
            print("")


    def display_top3_student(self):
        print("\nTop 3 Sudents in the class are: ")
        if(len(self.object_list)<3):
            n=len(self.object_list)
        else:
            n=3
        for i in range(0,n):
            temp=self.object_list[i].get_details()
            print(temp[2])