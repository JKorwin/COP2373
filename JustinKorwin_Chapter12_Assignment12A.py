# this program will create a file that stores student names and grades for 3 tests
# It will then read and present the data in a variety of ways
# importing CSV
import csv
import numpy as np

# defining function for collecting all the student data
def student_data_collect():
    # asking for number of student
    student_number = int(input("Please enter the number of students: "))

    # making data list with header of all the info that will be collected
    header = ['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3']
    data = [header]

    # getting the data for each of the students
    for x in range(student_number):
        first_name = input("Please enter the student's first name: ")
        last_name = input("Please enter the student's last name: ")
        exam1 = int(input("Please enter the student's grade from exam 1: "))
        exam2 = int(input("Please enter the student's grade from exam 2: "))
        exam3 = int(input("Please enter the student's grade from exam 3: "))

        # appending the student name and grades to the data list
        data.append([first_name, last_name, exam1, exam2, exam3])

        # now we can write the appended data to a csv file with the name grades.csv using writerows
        with open('grades.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(data)

# calling the student data collection function (i put this to a comment so i wouldn't have to keep typing in 10 names and sets of grades)
# student_data_collect()

# defining function that will load data into numpy array and show a bunch of stats
def numpy_data():
    with open('grades.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # putting data into list to put into numpy array
        data = list(csv_reader)

    # convert to numpy
    grades = np.array(data[1:])[:, 2:].astype(float)

    # calculating and printing the mean, median, minimum, maximum, and standard deviation for each exam
    for i in range(grades.shape[1]):
        print(f"\nStatistics for Exam {i + 1}:")
        print(f"Mean: {np.mean(grades[:, i])}")
        print(f"Median: {np.median(grades[:, i])}")
        print(f"Standard deviation: {np.std(grades[:, i])}")
        print(f"Minimum: {np.min(grades[:, i])}")
        print(f"Maximum: {np.max(grades[:, i])}")

    # now doing the same data set but for all exams with use of .flatten to make array 1 dimension (i.e. combine all exams)
    flattened_grades = grades.flatten()
    print("\nOverall statistics for all exams combined:")
    print(f"Mean: {np.mean(flattened_grades)}")
    print(f"Median: {np.median(flattened_grades)}")
    print(f"Standard Deviation: {np.std(flattened_grades)}")
    print(f"Minimum: {np.min(flattened_grades)}")
    print(f"Maximum: {np.max(flattened_grades)}")

    # determining how many passed and failed and then printing them
    pass_grade = 60
    total_passed = 0
    total_failed = 0
    for i in range(grades.shape[1]):
        passed = np.sum(grades[:, i] >= pass_grade)
        failed = np.sum(grades[:, i] < pass_grade)
        total_passed += passed
        total_failed += failed
        print(f"\nNumber of students who passed Exam {i + 1}: {passed}")
        print(f"Number of students who failed Exam {i + 1}: {failed}")

    # calculating pass percentage using total_passed and total_failed
    pass_percent = (total_passed / (total_passed + total_failed)) * 100
    print(f"\nPass percentage between all the exams: {pass_percent}%")


# calling numpy data function
numpy_data()