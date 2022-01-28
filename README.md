# Student performance program

>This is one of the coursework project to monitor student performance from their online test result.

## CW1
In CW1, a Python program to clean, format and store data in order to create an SQLite database for a student monitoring system.
## CW2
In CW2, there are several modules to monitor different student performance.

- Menu
  > A python main program which provides the required menu options to users for the program functionalities.

- DAFunction
  > A Python module which contains common functions that all modules use to carry out their functionalities.

- HardworkingStudent
  > A Python module which contains functions used to list hardworking students. The program should classify the students as hardworking if their grade of the summative online test is more than 60, and their rates are “Below Benninger” or “Beginner” in the StudentRate.csv file.

- StudentPerformance
  > A Python module which contains functions used to ask for student ID and the title of the test, that users wish to analyse. The function will find out student performance on each question of the assessment. Both relative and absolute performance. Absolute performance is a percentage grade (i.e., student grade out of 100). Relative performance is a distance number between student’s grade and test average.

- UnderperformingStudent
  > A Python module which allow users to find out the underperforming students.
    The underperforming criteria will be:
    - Students who got 1-50 for their summative test
    - Students also got 1-50 three times or more for formative tests.

- TestResult
  >  A Python module which allow users to find out individule student grades on all of the tests.
