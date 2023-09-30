import pandas as panda
import os
import shutil
# Importing Libraries
#mport numpy as np
#import matplotlib.pyplot as plt
#import pandas as pd

#import the datast
student_dataset = None  # initialize as None
row_cells = ""
column_cells = ""

def receive_file(file_name):
    global student_dataset  # use global keyword to update the global variable
    global csv_file
    global file
    global row_cells
    global column_cells

    file = file_name
    print(f"Received file {file}")

    # destination file (the copy you want to create)
    destination_file = f'NEW_{file}'

    # use shutil.copyfile to copy the source file to the destination
    global csv_file
    csv_file = shutil.copyfile(file, destination_file)

    print(f"Copy file {file} to {csv_file}")

    # Check if the file exists before reading it
    if file and panda.Series(csv_file).notna().all():
        student_dataset = panda.read_csv(csv_file)
        row_cells = student_dataset.iloc[:, :].values
        column_cells = student_dataset.iloc[:, 0].values
        return csv_file
    else:
        raise ValueError("No CSV file provided or invalid file name, please try again.")

#student_ids = student_dataset.iloc[:, 0].values
#student_connor = student_dataset.iloc[10, :-1].values
#print("All students: " + str(row_cells))
#print("student01: " + str(row_cells[0]))
#print("All Student ID" + str(column_cells))
#print(student_connor)

# for each of the averages we read in the values of hw, quiz, finnal, etc
def find_avg_hw(student_position_num):

    student_current = student_dataset.iloc[student_position_num, 4:7].values
    hw_amount = 0
    assignment_count=0
    hw_total_perc = 0

    for hw_score in student_current:
        assignment_count+=1
        hw_amount+=hw_score

    hw_total_perc = hw_amount/assignment_count
    return hw_total_perc

def find_avg_quiz(student_position_num):

    student_current = student_dataset.iloc[student_position_num, 7:11].values
    quiz_amount = 0
    quiz_count=0
    quiz_total_perc = 0

    #print("current student quiz grades are:"+str(student_current))

    for quiz_score in student_current:
        quiz_count+=1
        quiz_amount+=quiz_score

    quiz_total_perc = quiz_amount/quiz_count
    return quiz_total_perc

def find_avg_test(student_position_num):

    student_current = student_dataset.iloc[student_position_num, 11:13].values
    test_amount = 0
    test_count=0
    test_total_perc = 0

    #print("current student test grades are:"+str(student_current))

    for test_score in student_current:
        test_count+=1
        test_amount+=test_score

    test_total_perc = test_amount/test_count
    return test_total_perc

# used weights to go against the average grade, then found the rounded total

def find_weighted_score(hw_score, quiz_score, midterm_score, final_score):
    weighted_score = (hw_score*.2) + (quiz_score*.2) + (midterm_score*.3) + (final_score*.3)
    weighted_score = round(int(weighted_score), 2)
    return weighted_score

# calculates the letter grade
def find_letter_grade(weigthted_score):
    if weigthted_score >= 90:
        lettergrade = 'A'
    elif weigthted_score >= 80:
        lettergrade = 'B'
    elif weigthted_score >= 70:
        lettergrade = 'C'
    elif weigthted_score >= 60:
        lettergrade = 'D'
    else:
        lettergrade = 'F'
    return lettergrade

# displays output on terminal for the single or all display
def display_slate(student_curr_name, hw_score, quiz_score, midterm_score, final_score, weighted_score, lettergrade):
    print("=========================================================")
    print(f"{student_curr_name} HW score: {hw_score:.2f}")
    print(f"{student_curr_name} Quiz score: {quiz_score:.2f}")
    print(f"{student_curr_name} Midterm score: {int(midterm_score):.2f}")
    print(f"{student_curr_name} Final score: {int(final_score):.2f}")
    print(f"{student_curr_name} Weighted score: {weighted_score:.2f}")
    print(f"{student_curr_name} Final Grade: {lettergrade}")
    print("=========================================================")
    return

# more global identifiers used later
global amount_students
global all_student_id

def count_students():
    amount_students = len(row_cells)
    return amount_students

# takes in the range of rows - 1 (header), will call all functions above to get the details
# idea: can change this to take in specific values, like if connor is calles, he is student 12
# action: did this, success

def find_min_max_mean_column(column_name):
    if column_name in student_dataset:
        # Check if the column exists in the DataFrame
        data = student_dataset[column_name]
        min_score = data.min()
        max_score = data.max()
        mean_score = data.mean()
        print("=========================================================")
        print(f"The min, mean, and max for the {column_name} column are: {min_score}, {mean_score:.2f}, {max_score}")
        print("=========================================================")
        return
    else:
        print(f"Column '{column_name}' does not exist in the DataFrame.")

# reads in csv_file to open, stores rows and columns
def parse_all_students(amount_students):
    # update csv file
    #csv_file = 'Student_data.csv'
    if csv_file:
        student_dataset = panda.read_csv(csv_file)
        row_cells = student_dataset.iloc[:, :].values
        column_cells = student_dataset.iloc[:, 0].values
        amount_students = len(row_cells)
        #print(amount_students)
        print(student_dataset)
    else:
        raise ValueError(f"No csv file imported")


    print(f"parse function hit:{amount_students} student files")
    
    for i in range(0, amount_students):
        if i >= len(row_cells):  # double check if the index is valid
            break  # exit the loop if the index is out of bounds

        # storing student vals
        first = student_dataset.iloc[i, 1]
        last = student_dataset.iloc[i, 2]
        student_curr_name = first+' '+last

        # calculating avg score using functions
        hw_score = find_avg_hw(i)
        quiz_score = find_avg_quiz(i)
        midterm_score = student_dataset.iloc[i, 11:12].values[0]  # Access the value from the Series
        final_score = student_dataset.iloc[i, 12:13].values[0]  # Access the value from the Series
        weighted_score = find_weighted_score(hw_score, quiz_score, midterm_score, final_score)
        lettergrade = find_letter_grade(weighted_score)
        display_slate(student_curr_name, hw_score, quiz_score, midterm_score, final_score, weighted_score, lettergrade)
    return

# used purely from pase by id
def parse_single_students(row_number):
    row_number = int(row_number)
    first = student_dataset.iloc[row_number, 1]
    last = student_dataset.iloc[row_number, 2]
    student_curr_name = first+' '+last
    hw_score = find_avg_hw(row_number)
    quiz_score = find_avg_quiz(row_number)
    midterm_score = student_dataset.iloc[row_number, 11:12].values
    final_score = student_dataset.iloc[row_number, 12:13].values
    weighted_score = find_weighted_score(hw_score, quiz_score, midterm_score, final_score)
    lettergrade = find_letter_grade(weighted_score)
    # final_score = (hw_score*hw_percenage) + (quiz_score*quiz_percenage) + (test_score*test_percenage)
    display_slate(student_curr_name, hw_score, quiz_score, midterm_score, final_score, weighted_score, lettergrade)


def parse_by_id_students(student_id):
    student_dataset = panda.read_csv(csv_file)
    where_student = 0
    all_student_id = student_dataset.iloc[:, 0].values
    # print(all_student_id)
    for id in all_student_id:
        #print("current id: "+str(id)+" vs comparative id: "+ str(student_id))
        slate = int(id)
        if slate == student_id:
            #print("hit")
            break
        where_student+=1
    return where_student
    #parse_single_students(where_student)

# reads and restores the global file
def delete_student(num_student):
    #csv_file = 'Student_data.csv' used for testing
    student_dataset = panda.read_csv(csv_file)
    row_cells = student_dataset.iloc[:, :].values
    column_cells = student_dataset.iloc[:, 0].values
    #num_student = input("Please enter the id of the student you would like to drop: ")
    for student_id in student_dataset['SID']:
        #print(f"student_id {student_id} match goal {num_student}")
        if student_id == int(num_student):
            row_num = parse_by_id_students(int(num_student))
            print("Row num of student: " + str(row_num))
            student_dataset.drop(row_num, axis=0, inplace=True)
            student_dataset.to_csv(csv_file, index=False)
            # rwset row counts for parsing
            student_dataset.reset_index(drop=True, inplace=True)
            row_cells = student_dataset.iloc[:, :].values
            amount_students = len(row_cells)
            return amount_students
    raise ValueError(f'No student with id {num_student}')

def modify_student(num_student, score, assignment):
    old_score = student_dataset.at[num_student, assignment]
    student_dataset.at[num_student, assignment] = score
    student_dataset.to_csv(csv_file, index=False)
    print(f"Row {num_student} was modified: Changed {assignment} score to {score} from {old_score}")


def add_student(SID, first_name, last_name, email, hw01, hw02, hw03, quiz01, quiz02, quiz03, quiz04, midterm, final):
    global student_dataset

    new_entry = {
        'SID': SID,   
        'FirstName': first_name,
        'LastName': last_name,
        'Email': email,
        'HW1': int(hw01),
        'HW2': int(hw02),
        'HW3': int(hw03),
        'Quiz1': int(quiz01),
        'Quiz2': int(quiz02),
        'Quiz3': int(quiz03),
        'Quiz4': int(quiz04),
        'MidtermExam': int(midterm),
        'FinalExam': int(final)
    }

    # Create a new DataFrame with the new_entry
    new_row = panda.DataFrame(new_entry, index=[0])

    # Concatenate the new row with the existing DataFrame
    student_dataset = panda.concat([student_dataset, new_row], ignore_index=True)

    # Write the updated back to the CSV file
    student_dataset.to_csv(csv_file, index=False)

    global amount_students
    row_cells = student_dataset.iloc[:, :].values
    amount_students = len(row_cells)
    print("Updated values students:" + str(amount_students))
    #print(student_dataset)
    return amount_students


#print("Connor avg hw score: " + str(find_avg_hw(10)))


#parse all students example
        #print(parse_all_students(amount_students))

#single id search example
        #print(parse_single_students(parse_by_id_students(23941)))

#delete example
        #print(amount_students)
        #new_count = delete_student()
        #print(new_count)
        #print(parse_all_students(new_count))

#print(parse_single_students(parse_by_id_students(23941)))

#print(parse_all_students())

#find_min_max_mean_column("HW1")

# TO, DO
# modifying of grades within csv file
