

from person import Person


class Student(Person): 

    def __init__(self, lastName, firstName, age, studentID):
        super().__init__(lastName, firstName, age) 
        self.studentID = studentID
    
    def __str__(self):
        return f"student name: {self.firstName}, {self.lastName} and student id: {self.studentID}"