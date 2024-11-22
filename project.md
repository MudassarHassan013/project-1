# Student Performance Tracker

This project consists of two classes, `Student` and `PerformanceTracker`, designed to manage and track student scores, calculate their average scores, determine pass/fail status, and display individual and class-wide performance.

## Project Overview

The `Student` class stores individual student information, including their name and scores across different subjects. The `PerformanceTracker` class manages multiple students, calculates the class average, and displays each student’s performance details.

## Class Structure and Functions

### 1. `Student` Class

The `Student` class represents an individual student, storing their name and scores across subjects.

#### `__init__(self, name, scores)`

- **Purpose**: Initializes a `Student` instance with the student’s `name` and `scores`.
- **Parameters**:
  - `name` (str): The student’s name.
  - `scores` (dict): A dictionary with subjects as keys and scores as values.

#### `calculate_average(self)`

- **Purpose**: Calculates the student’s average score across subjects.
- **Error Handling**:
  - Catches `TypeError` if scores are not numerical.
  - Catches `ZeroDivisionError` if there are no subjects in the dictionary.

#### `pass_fail(self)`

- **Purpose**: Determines if the student has passed or failed based on an average score of 40 or higher.

### 2. `PerformanceTracker` Class

The `PerformanceTracker` class manages multiple `Student` instances and performs class-wide calculations.

#### `__init__(self)`

- **Purpose**: Initializes an empty list to store `Student` instances.

#### `add_student(self, student)`

- **Purpose**: Adds a `Student` instance to the list.
- **Error Handling**: Prints an error if the input is not a `Student` instance.

#### `calculate_class_average(self)`

- **Purpose**: Calculates the average score for the class.
  
#### `display_student_performance(self)`

- **Purpose**: Displays each student’s name, subject scores, average score, and pass/fail status.

## Example Usage

1. **Create Student Instances**:
   ```python
   student1 = Student("Alice", {"Math": 85, "Science": 78, "English": 92})
   student2 = Student("Bob", {"Math": 56, "Science": 49, "English": 65})
   student3 = Student("Charlie", {"Math": 30, "Science": 42, "English": 38})
