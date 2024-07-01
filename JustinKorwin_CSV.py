# this program will create a file that stores student names and grades for 3 tests
# It will then read and present the data in a tabular format
# importing CSV
import csv

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

# calling the student data collection function
student_data_collect()

# now that the data is in a file I can make a function that reads and displays the data in a tabular format
# creating read function
def data_read():
    # opening the file in read mode now
    with open('grades.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # converting read data to a list because I actually know how to deal with lists
        data = list(csv_reader)

        # acknowledging first line of list is header then printing the header in good tabular format
        header = data[0]
        print(f"{header[0]:<20} {header[1]:<20} {header[2]:<10} {header[3]:<10} {header[4]:<10}")

        # printing all the data real easy because lists are so cool
        for x in data[1:]:
            print(f"{x[0]:<20} {x[1]:<20} {x[2]:<10} {x[3]:<10} {x[4]:<10}")
# calling data read function
data_read()