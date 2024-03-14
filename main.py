from student import Student
from course import Course

courseList = []

student = Student("Smith", "Christina", 22, 99999, courseList)
course1 = Course("PROG12583", "Python")
course2 = Course("PROG23863", "OOP - Java")
course3 = Course("MATH18584", "Computer Math")
course4 = Course("SYST15123", "Operating Systems Linux")
course5 = Course("TELE13167", "Introduction to Data Communications and Networking")
course6 = Course("TELE20483", "Cloud Enabled Networks")

# def addCourseToList(courses, course):
#     if course not in courses:
#         courses.append(course)


def displayCoursesList(courses):
    for index in range(len(courses)):
        print(courses[index])



student.addCourseToList(course1)
displayCoursesList(student.courses)






