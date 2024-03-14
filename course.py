class Course:
    def __init__(self, courseCode, courseName):
        self.courseCode = courseCode
        self.courseName = courseName

    def __str__(self):
        return f"The course code: {self.courseCode} which is {self.courseName}"