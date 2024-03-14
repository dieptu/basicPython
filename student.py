

from person import Person


class Student(Person): 

    def __init__(self, lastName, firstName, age, studentID, courses):
        super().__init__(lastName, firstName, age) 
        self.studentID = studentID
        self.courses = courses
    
    def __str__(self):
        return f"student name: {self.firstName}, {self.lastName} and student id: {self.studentID}"
    
    def addCourseToList(self, course):
        if course not in self.courses:
            self.courses.append(course)