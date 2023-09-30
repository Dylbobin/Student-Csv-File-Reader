import sys
import time
import tkinter as tk
import os
from tkinter import filedialog
import import_data_find_students as head
import shutil

# Function to handle importing a CSV file
#global amount_students
amount_students = head.count_students()
csv_file_name = None

def give_file(file_name):
    global csv_file_name
    csv_file_name = head.receive_file(file_name)
    print(f"Recieved file {csv_file_name}")


def import_csv():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        import_label.config(text="Import Success file path: " + file_path)
        import_label.pack()
        global csv_file_name

        csv_file = os.path.basename(file_path)
        give_file(csv_file)

def export_csv():
    import_label.pack_forget()
    if csv_file_name:
        export_label.config(text="Export Success in current file path, file name: " + csv_file_name)
        export_label.pack()
        time.sleep(3)
        raise SystemExit("Exiting the program")
    export_label.config(text="No Path or CSV file created")
    export_label.pack()
    time.sleep(1)
    raise SystemExit("No CSV file created, Exiting the program")

#amount_students = head.count_students()

# Function to handle the search criteria based on user input

def search_criteria():
    #remove import label
    import_label.pack_forget()
    # search by student id grab
    student_id = student_id_entry.get()
    #drop student grab
    drop_student_id_entry = drop_student_entry.get()
    #saearch assignment grab
    assignment_name = assignment_entry.get()
    # modify student ID
    modify_student_id = modify_student_entry.get()
    modify_score = modify_student_score_entry.get()
    modify_assignment = modify_student_assignment_entry.get()

    #add student grabs
    add_student_id = add_student_sid_entry.get()
    add_student_first_name = add_student_first_name_entry.get()
    add_student_last_name = add_student_last_name_entry.get()
    add_student_email = add_student_email_entry.get()
    add_student_hw01 = add_student_hw01_entry.get()
    add_student_hw02 = add_student_hw02_entry.get()
    add_student_hw03 = add_student_hw03_entry.get()
    add_student_quiz01 = add_student_quiz01_entry.get()
    add_student_quiz02 = add_student_quiz02_entry.get()
    add_student_quiz03 = add_student_quiz03_entry.get()
    add_student_quiz04 = add_student_quiz04_entry.get()
    add_student_midterm = add_student_midterm_entry.get()
    add_student_final = add_student_final_entry.get()

    #print(amount_students)  # Print the current value of amount_students

    if drop_student_checked.get() == 1:
        # If "Delete Student" checkbox is checked
        if drop_student_id_entry:
            print(f"Dropping student {drop_student_id_entry} from list")
            global amount_students
            amount_students = head.delete_student(drop_student_id_entry)  # Update amount_students
            print(f"Remaining student entrie: {amount_students}")
        else:
            assignment_error.config(text="Student Id needs to be provided/Needs a match")
    elif modify_student_checked.get() == 1:
        # If "Modify Student" checkbox is checked
        if modify_student_id and modify_score and modify_assignment:
            modify_student_error.config(text=f"Modify Student ID: {modify_student_id}")
            modify_student_id = int(modify_student_id)
            student_data_text.config(text=head.modify_student(head.parse_by_id_students(modify_student_id), modify_score, modify_assignment))
        else:
            modify_student_error.config(text="Student ID is required when Modifyingy Student")
    elif add_student_checked.get() == 1:
        # If "Delete Student" checkbox is checked
        if add_student_id and add_student_first_name and add_student_last_name and add_student_email:
            print(f"Adding student {add_student_id} to list")
            amount_students = head.add_student(add_student_id, add_student_first_name, add_student_last_name, 
                                               add_student_email, add_student_hw01, add_student_hw02, add_student_hw03, 
                                               add_student_quiz01, add_student_quiz02, add_student_quiz03, add_student_quiz04, 
                                               add_student_midterm, add_student_final)  # Update amount_students
            print(amount_students)
        else:
            assignment_error.config(text="At least Student Id, First Name, Last Name, and Email needs to be provided to create student")
    elif display_all_var.get() == 1:
        # If "Display All" checkbox is checked
        print("Display All is checked")
        amount_students = head.count_students()
        #print(amount_students)
        head.parse_all_students(amount_students)
        # Implement logic to read the CSV file and display all entries
    elif search_by_student_id_checked.get() == 1:
        # If "Search by Student ID" checkbox is checked
        if student_id:
            student_id_success.config(text=f"Search by Student ID is checked. Student ID: {student_id}")
            student_id = int(student_id)
            student_data_text.config(text=head.parse_single_students(head.parse_by_id_students(student_id)))
        else:
            student_id_error.config(text="Student ID is required when searching by Student")
    elif search_by_assignment_checked.get() == 1:
        # If "Search by Assignment" checkbox is checked
        print(assignment_name)
        if assignment_name:
            print(head.find_min_max_mean_column(assignment_name))
        else:
            assignment_error.config(text="Assignment name is required when searching by Assignment")
    else:
        # If neither option is checked
        print("Neither option is checked")


# Function to toggle the visibility of the student ID entry field
def toggle_student_id_entry():
    if search_by_student_id_checked.get() == 1:
        # If "Search by Student ID" checkbox is checked
        student_id_label.pack()
        student_id_entry.pack()
        student_id_entry.config(highlightbackground="white", highlightthickness=2)
        student_id_error.config(text="")
    else:
        # If "Search by Student ID" checkbox is not checked
        student_id_label.pack_forget()
        student_id_entry.pack_forget()
        student_id_error.config(text="")

def toggle_assignment_entry():
    if search_by_assignment_checked.get() == 1:
        # If "Search by Assignment" checkbox is checked
        assignment_label.pack()
        assignment_entry.pack()
        assignment_entry.config(highlightbackground="white", highlightthickness=2)
    else:
        # If "Search by Assignment" checkbox is not checked
        assignment_label.pack_forget()
        assignment_entry.pack_forget()
        assignment_error.config(text="")

def toggle_add_student_entry():
    if add_student_checked.get() == 1:
        # If "Add Student" checkbox is checked
        add_student_sid_label.pack()
        add_student_sid_entry.pack()
        add_student_sid_entry.config(highlightbackground="white", highlightthickness=2)

        add_student_first_name_label.pack()
        add_student_first_name_entry.pack()
        add_student_first_name_entry.config(highlightbackground="white", highlightthickness=2)

        add_student_last_name_label.pack()
        add_student_last_name_entry.pack()
        add_student_last_name_entry.config(highlightbackground="white", highlightthickness=2)

        add_student_email_label.pack()
        add_student_email_entry.pack()
        add_student_email_entry.config(highlightbackground="white", highlightthickness=2)

        add_student_hw01_label.pack()
        add_student_hw01_entry.pack()
        add_student_hw01_entry.config(highlightbackground="white", highlightthickness=2)

        add_student_hw02_label.pack()
        add_student_hw02_entry.pack()
        add_student_hw02_entry.config(highlightbackground="white", highlightthickness=2)

        add_student_hw03_label.pack()
        add_student_hw03_entry.pack()
        add_student_hw03_entry.config(highlightbackground="white", highlightthickness=2)

        add_student_quiz01_label.pack()
        add_student_quiz01_entry.pack()
        add_student_quiz01_entry.config(highlightbackground="white", highlightthickness=2)

        add_student_quiz02_label.pack()
        add_student_quiz02_entry.pack()
        add_student_quiz02_entry.config(highlightbackground="white", highlightthickness=2)

        add_student_quiz03_label.pack()
        add_student_quiz03_entry.pack()
        add_student_quiz03_entry.config(highlightbackground="white", highlightthickness=2)

        add_student_quiz04_label.pack()
        add_student_quiz04_entry.pack()
        add_student_quiz04_entry.config(highlightbackground="white", highlightthickness=2)

        add_student_midtern_label.pack()
        add_student_midterm_entry.pack()
        add_student_midterm_entry.config(highlightbackground="white", highlightthickness=2)

        add_student_final_label.pack()
        add_student_final_entry.pack()
        add_student_final_entry.config(highlightbackground="white", highlightthickness=2)
        add_student_error.config(text="")
    else:
        # If "Add Student" checkbox is not checked
        add_student_sid_label.pack_forget()
        add_student_sid_entry.pack_forget()
        add_student_error.config(text="")

        add_student_first_name_label.pack_forget()
        add_student_first_name_entry.pack_forget()

        add_student_last_name_label.pack_forget()
        add_student_last_name_entry.pack_forget()

        add_student_email_label.pack_forget()
        add_student_email_entry.pack_forget()

        add_student_hw01_label.pack_forget()
        add_student_hw01_entry.pack_forget()

        add_student_hw02_label.pack_forget()
        add_student_hw02_entry.pack_forget()

        add_student_hw03_label.pack_forget()
        add_student_hw03_entry.pack_forget()

        add_student_quiz01_label.pack_forget()
        add_student_quiz01_entry.pack_forget()

        add_student_quiz02_label.pack_forget()
        add_student_quiz02_entry.pack_forget()

        add_student_quiz03_label.pack_forget()
        add_student_quiz03_entry.pack_forget()

        add_student_quiz04_label.pack_forget()
        add_student_quiz04_entry.pack_forget()

        add_student_midtern_label.pack_forget()
        add_student_midterm_entry.pack_forget()

        add_student_final_label.pack_forget()
        add_student_final_entry.pack_forget()

# Function to toggle the visibility of the student ID entry field for "Drop Student" button
def toggle_drop_student_entry():
    if drop_student_checked.get() == 1:
        # If "Drop Student" checkbox is checked
        drop_student_label.pack()
        drop_student_entry.pack()
        drop_student_entry.config(highlightbackground="white", highlightthickness=2)
        drop_student_error.config(text="")
    else:
        # If "Drop Student" checkbox is not checked
        drop_student_label.pack_forget()
        drop_student_entry.pack_forget()
        drop_student_error.config(text="")

def toggle_modify_student_entry():
    if modify_student_checked.get() == 1:
        # If "Drop Student" checkbox is checked
        modify_student_label.pack()
        modify_student_entry.pack()
        modify_student_entry.config(highlightbackground="white", highlightthickness=2)
        modify_student_assignment.pack()
        modify_student_assignment_entry.pack()
        modify_student_assignment_entry.config(highlightbackground="white", highlightthickness=2)
        modify_student_score.pack()
        modify_student_score_entry.pack()
        modify_student_score_entry.config(highlightbackground="white", highlightthickness=2)
        modify_student_error.config(text="")
    else:
        # If "Drop Student" checkbox is not checked
        modify_student_label.pack_forget()
        modify_student_entry.pack_forget()
        modify_student_assignment_entry.pack_forget()
        modify_student_score_entry.pack_forget()
        modify_student_score.pack_forget()
        modify_student_assignment.pack_forget()
        modify_student_error.config(text="")

# Create the main window
root = tk.Tk()
root.title("CSV Student Search")
root.geometry("1300x950")
root.configure(bg="light blue")

# Create and place the Export button
export_button = tk.Button(root, text="Export", command=export_csv, bg="white", fg="black")
export_button.pack(side='bottom', anchor='center')
export_label = tk.Label(root, text="", bg="light blue", fg="black")

# Create and place the import button and label
import_button = tk.Button(root, text="Import", command=import_csv, bg="white", fg="black")
import_button.pack(pady=10)
import_label = tk.Label(root, text="", bg="light blue", fg="black")

# Create and place the entry box for "Display All" checkbox
display_all_var = tk.IntVar()
display_all_checkbox = tk.Checkbutton(root, text="Display All", variable=display_all_var, bg="light blue", fg="black")
display_all_checkbox.pack()

# Create a variable to hold the state of the "Search by Student ID" checkbox
search_by_student_id_checked = tk.IntVar()
student_id_checkbox = tk.Checkbutton(root, text="Search by Student ID", variable=search_by_student_id_checked, bg="light blue", fg="black", command=toggle_student_id_entry)
student_id_checkbox.pack()

# Create a variable to hold the state of the "Search by Assignment" checkbox
search_by_assignment_checked = tk.IntVar()
assignment_checkbox = tk.Checkbutton(root, text="Search by Assignment", variable=search_by_assignment_checked, bg="light blue", fg="black", command=toggle_assignment_entry)
assignment_checkbox.pack()

# Set the initial value of the "Search by Assignment" checkbox to 0 (unchecked)
search_by_assignment_checked.set(0)

# Create an entry field for entering student ID
student_id_label = tk.Label(root, text="Enter Student ID:", bg="light blue", fg="black")

assignment_label = tk.Label(root, text="Enter assignment name:", bg="light blue", fg="black")

student_id_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)
assignment_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)

student_id_success = tk.Label(root, text="", fg="black", bg="light blue")
student_id_success.pack()

student_id_error = tk.Label(root, text="", fg="red", bg="light blue")
student_id_error.pack()

assignment_error = tk.Label(root, text="", fg="red", bg="light blue")
assignment_error.pack()

student_data_text = tk.Label(root, text="", fg="Black", bg="White")

modify_student_error = tk.Label(root, text="", fg="red", bg="light blue")
modify_student_error.pack()

modify_student_success = tk.Label(root, text="", fg="Black", bg="light blue")
modify_student_success.pack()

# Create variables to hold the state of the "Add Student" and "Drop Student" checkboxes
add_student_checked = tk.IntVar()
add_student_checkbox = tk.Checkbutton(root, text="Add Student", variable=add_student_checked, bg="light blue", fg="black", command=toggle_add_student_entry)
add_student_checkbox.pack()

drop_student_checked = tk.IntVar()
drop_student_checkbox = tk.Checkbutton(root, text="Drop Student", variable=drop_student_checked, bg="light blue", fg="black", command=toggle_drop_student_entry)
drop_student_checkbox.pack()

modify_student_checked = tk.IntVar()
modify_student_checkbox = tk.Checkbutton(root, text="Modify Student", variable=modify_student_checked, bg="light blue", fg="black", command=toggle_modify_student_entry)
modify_student_checkbox.pack()

modify_student_label = tk.Label(root, text="Enter Student ID to Modify:", bg="light blue", fg="black")
modify_student_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)

modify_student_assignment = tk.Label(root, text="Enter Assignment Name to Modify:", bg="light blue", fg="black")
modify_student_assignment_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)

modify_student_score = tk.Label(root, text="Enter Assignment Score:", bg="light blue", fg="black")
modify_student_score_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)
# Set the initial values of the "Add Student" and "Drop Student" checkboxes to 0 (unchecked)
add_student_checked.set(0)
drop_student_checked.set(0)

# Create labels and entry widgets for each field
add_student_sid_label = tk.Label(root, text="Enter Student ID to Add:", bg="light blue", fg="black")
add_student_sid_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)

add_student_first_name_label = tk.Label(root, text="Enter First Name:", bg="light blue", fg="black")
add_student_first_name_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)

add_student_last_name_label = tk.Label(root, text="Enter Last Name:", bg="light blue", fg="black")
add_student_last_name_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)

add_student_email_label = tk.Label(root, text="Enter Email:", bg="light blue", fg="black")
add_student_email_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)

add_student_hw01_label = tk.Label(root, text="Enter HW01:", bg="light blue", fg="black")
add_student_hw01_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)

add_student_hw02_label = tk.Label(root, text="Enter HW02:", bg="light blue", fg="black")
add_student_hw02_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)

add_student_hw03_label = tk.Label(root, text="Enter HW03:", bg="light blue", fg="black")
add_student_hw03_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)

add_student_quiz01_label = tk.Label(root, text="Enter Quiz01:", bg="light blue", fg="black")
add_student_quiz01_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)

add_student_quiz02_label = tk.Label(root, text="Enter Quiz02:", bg="light blue", fg="black")
add_student_quiz02_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)

add_student_quiz03_label = tk.Label(root, text="Enter Quiz03:", bg="light blue", fg="black")
add_student_quiz03_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)

add_student_quiz04_label = tk.Label(root, text="Enter Quiz04:", bg="light blue", fg="black")
add_student_quiz04_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)

add_student_midtern_label = tk.Label(root, text="Enter Midterm:", bg="light blue", fg="black")
add_student_midterm_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)

add_student_final_label = tk.Label(root, text="Enter Final:", bg="light blue", fg="black")
add_student_final_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)

# Drop student widget
drop_student_label = tk.Label(root, text="Enter Student ID to Drop:", bg="light blue", fg="black")
drop_student_entry = tk.Entry(root, highlightbackground="white", highlightthickness=2)

add_student_error = tk.Label(root, text="", fg="red", bg="light blue")
drop_student_error = tk.Label(root, text="", fg="red", bg="light blue")
modify_student_error = tk.Label(root, text="", fg="red", bg="light blue")

# Create a button to trigger the search
search_button = tk.Button(root, text="Search Criteria", command=search_criteria, bg="white", fg="black")
search_button.place(x=1100, y=10)

# Start the main loop
root.mainloop()
