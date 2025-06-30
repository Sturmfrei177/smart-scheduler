# List to store exam schedules
exam_schedule = []

# Function to add a new exam
def add_exam():
    print("\nAdd New Exam")
    name = input("Enter exam name: \n")
    date = input("Enter exam date (MM-DD): \n")
    time = input("Enter exam time (HH:MM): \n")
    room = input("Enter exam room: ")
    
    # Create exam dictionary
    exam = {
        "name": name,
        "date": date,
        "time": time,
        "room": room
    }
    
    # Add exam to schedule
    exam_schedule.append(exam)
    print("Exam successfully added!\n")

# Function to view all exams
def view_exams():
    print("\nView Exam Schedule")
    if not exam_schedule:
        print("No Exam Scheduled\n")
        return
    
    for index, exam in enumerate(exam_schedule):
        print(f"{index + 1}. {exam['name']} on {exam['date']} at {exam['time']} in {exam['room']}")
    print()

# Function to edit an exam
def edit_exam():
    view_exams()
    if not exam_schedule:
        return
    
    try:
        #Asks the user to enter the index(e.g: 1) to edit
        exam_index = int(input("Enter the exam index to edit: ")) - 1
        
        if 0 <= exam_index < len(exam_schedule):
            print("\nLeave field blank to keep current value.")
            
            # Get current values
            current_exam = exam_schedule[exam_index]
            
            # Prompt for new values
            name = input(f"New name (current: {current_exam['name']}): ") or current_exam['name']
            date = input(f"\nNew date (current: {current_exam['date']}): ") or current_exam['date']
            time = input(f"\nNew time (current: {current_exam['time']}): ") or current_exam['time']
            room = input(f"\nNew room (current: {current_exam['room']}): ") or current_exam['room']
            
            # Update the selected exam
            exam_schedule[exam_index] = {
                "name": name,
                "date": date,
                "time": time,
                "room": room
            }
            print("Exam updated successfully!\n")
        else:
            print("Invalid exam index.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
 #Delete Exam       
def delete_exam():
    if not exam_schedule:
        #If there are no exams added
        print("\nNo exams to delete.\n")
        return
#Similar to "View Exams", this shows the list of exams to delete.
    print("\nDelete Exam")
    for index, exam in enumerate(exam_schedule):
        print(f"{index + 1}. {exam['name']} on {exam['date']} at {exam['time']} in {exam['room']}")

    try:
 #Prompts the user to input the index of the schedule they want to delete
        exam_index = int(input("Enter the exam index to delete: ")) - 1
        if 0 <= exam_index < len(exam_schedule):
            deleted_exam = exam_schedule.pop(exam_index)
 #Prints when the exam has been deleted successfully.
            print(f"Exam '{deleted_exam['name']}' deleted successfully!\n")
        else:
 #Prints if the user inputed an invalid index(Not in the choices)
            print("Invalid exam index.\n")
    except ValueError:
 #Prints if the user inputed a letter, word, phrase or symbol.
        print("Invalid input. Please enter a valid number.\n")

# Example simple menu to test it:
def main():
#Main function and main menu for the system
    while True:
        print("1. Add Exam")
        print("2. View Exams")
        print("3. Edit Exam")
        print("4. Delete Exam")
        print("5. Exit")
#Asks the user to input the index of their choice
        choice = input("Choose an option: ")
        #Calls to open "Add Exam"
        if choice == "1":
            add_exam()
        #Calls to open "View Exams"
        elif choice == "2":
            view_exams()
        #Calls to open "Edit Exams"
        elif choice == "3":
            edit_exam()
        #Calls to open "Delete Exams"
        elif choice == "4":
            delete_exam()
        #Exits/Stops Program
        elif choice == "5":
            print("Goodbye!")
            break
        else:
 #Asks the user for an input again if the choice is not in the choices
            print("Invalid choice. Try again.\n")

# Run the main menu
main()