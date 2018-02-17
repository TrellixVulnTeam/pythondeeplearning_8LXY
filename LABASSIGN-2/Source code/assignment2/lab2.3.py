class Student:  # Class #1
    overall_total = 0

    def __init__(self):  # use of __init__ method
        self.full_name = input('Enter the name of the student ')
        self.rollno = input('Enter the umkcid')
        Student.overall_total += 1

    def count(self):    # Defining a function inside a class
        print('The number of students enrolled are ', Student.overall_total)

    def display(self):
        print('The name of the student is ', self.full_name)
        print('The umkcid of the student is ', self.rollno)


class TransferStudent(Student):  # Class #2

    def __init__(self):
        super(TransferStudent, self).__init__()  # use of super() call
        self.TransferredCredits = input('Enter the number of credits that are transferred')


class System:  # Class #3

    def __init__(self):
        self.TypeOfSystem = input('Enter the system online or inclass: ')

    def display(self):
        print('The system the student enrolled is: ', self.TypeOfSystem)


class Grades(TransferStudent):  # Class #4

    def __init__(self, grade, credits):
        TransferStudent.__init__(self)  # Another way of inheriting the parent class
        self.Grades = grade
        self.EnrolledCredits = credits

    def TotalCredits(self):
        self.TotalCreditsEnrolled = self.TransferredCredits + credits
        print('The total number of credits completed: ', self.TotalCreditsEnrolled)

    def display(self):
        print('The name of the student is ', self.full_name)
        print('The umkcid of the student is ', self.rollno)
        print('The Transferred credits are: ', self.TransferredCredits)
        print('The total number of credits enrolled: ', self.EnrolledCredits)
        print('The Grade obtained: ', self.Grades)


class Attendance:  # Class #5

    def __init__(self, percentage):
        self.__attendance = percentage  # Declaration of the private data member
        if self.__attendance < 64:
            print("Student's attendance is low")


# Creating the instances of all the classes

Student1 = Student()
Student2 = Student()
Student3 = Student()

Student4 = TransferStudent()
Student5 = TransferStudent()

Student6 = Grades("A+", "15")
Student7 = Grades("A", "5")

Student8 = Attendance(63)

Student7.display()

Student5.display()

Student7.count()
Student1.display()