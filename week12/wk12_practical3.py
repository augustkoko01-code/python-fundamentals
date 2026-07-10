# Student class

class Student:
    def __init__(self, name, marks):
        self.name = name      # Store the student's name
        self.marks = marks    # Store the student's marks

    def __str__(self):
        return f'{self.name} - {self.grade()}'   # Return the name and grade when printed

    def grade(self):
        # Return the grade based on the marks
        if self.marks >= 80:
            return 'A'
        elif self.marks >= 70:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        else:
            return 'F'

# Create a Student object for Peter with 85 marks
s1 = Student("Peter", 85)

# Create a Student object for John with 72 marks
s2 = Student("John", 72)

print(s1)   # Print Peter's name and grade
print(s2)   # Print John's name and grade