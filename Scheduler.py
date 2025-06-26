# List to store exam schedules
exam_schedule = []

# Function to add a new exam
def add_exam():
    print("\nAdd New Exam")
    name = input("Enter exam name: ")
    date = input("Enter exam date (MM-DD): ")
    time = input("Enter exam time (HH:MM): ")
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
        exam_index = int(input("Enter the exam index to edit: ")) - 1
        
        if 0 <= exam_index < len(exam_schedule):
            print("\nLeave field blank to keep current value.")
            
            # Get current values
            current_exam = exam_schedule[exam_index]
            
            # Prompt for new values
            name = input(f"New name (current: {current_exam['name']}): ") or current_exam['name']
            date = input(f"New date (current: {current_exam['date']}): ") or current_exam['date']
            time = input(f"New time (current: {current_exam['time']}): ") or current_exam['time']
            room = input(f"New room (current: {current_exam['room']}): ") or current_exam['room']
            
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

# Example simple menu to test it:
def main():
    while True:
        print("1. Add Exam")
        print("2. View Exams")
        print("3. Edit Exam")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_exam()
        elif choice == "2":
            view_exams()
        elif choice == "3":
            edit_exam()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run the main menu
main()
