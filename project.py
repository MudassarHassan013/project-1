# Creating a student class
class Student:

    # Creating a function to store student's name and scores in subjects
    def __init__(self, name, scores): # Changed _init_ to __init__
        self.name = name
        self.scores = scores

    # Creating a function to calculate average of scores
    def calculate_average(self):
        try:
            total = sum(self.scores.values())
            average = total / len(self.scores)
            return average
        except TypeError:
            print("Error: Scores must be numerical values.")
            return None
        except ZeroDivisionError:
            print("Error: Cannot calculate average with zero subjects.")
            return None

    # Creating a function to check if the student is passing or not
    def pass_fail(self):
        average = self.calculate_average()
        if average is not None and average >= 40:
            return "Pass"
        else:
            return "Fail"


# Creating a performance tracker class
class PerformanceTracker:

    # Initializing an empty list to store students
    def __init__(self): # Changed _init_ to __init__
        self.students = []

    # Creating a function to add students
    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            print("Error: Input must be a Student instance.")

    # Creating a function to calculate class average
    def calculate_class_average(self):
        total_average = 0
        for student in self.students:
            average = student.calculate_average()
            if average is not None:
                total_average += average
        return total_average / len(self.students) if self.students else 0

    # Creating a function to display students' performance
    def display_student_performance(self):
        for student in self.students:
            print("Name:", student.name)
            for subject, score in student.scores.items():
                print(f"{subject}: {score}")
            average = student.calculate_average()
            if average is not None:
                print("Average:", average)
            print("Status:", student.pass_fail())
            print("-" * 20)


# Example usage
# Creating Student instances
student1 = Student("Alice", {"Math": 85, "Science": 78, "English": 92})
student2 = Student("Bob", {"Math": 56, "Science": 49, "English": 65})
student3 = Student("Charlie", {"Math": 30, "Science": 42, "English": 38})

# Creating PerformanceTracker instance and adding students
tracker = PerformanceTracker()
tracker.add_student(student1)
tracker.add_student(student2)
tracker.add_student(student3)

# Displaying student performance
tracker.display_student_performance()

# Calculating and displaying class average
print("Class Average:", tracker.calculate_class_average())