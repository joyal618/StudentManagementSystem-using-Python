from controller import Controller

count=0
class View:
    controller= Controller()
    @staticmethod
    def switch(argument):
        if(argument==1):
            View.controller.add_student()
            View.main()
        elif(argument==2):
            View.controller.display_student()
            View.main()
        elif(argument==3):
            View.controller.display_top3_student()
        elif(argument==4):
            exit()
        else:
            print ("Wrong Input.. Try Again!!")
    @classmethod
    def main(cls):
        while 1:
            cls.switch(int(input("\nEnter an option: \n\t1. Insert a new student\n\t2. List the students\n\t3. List 3 students with top marks\n\t4. Exit\n\t\t~")))









if __name__ == "__main__":
    View.main()