import functions

while True:
    data = functions.load_data()
    print("Welcome to the CLI Cardio Tracker!")
    print("\nMenu:")
    print("1. Log Workout")
    print("2. View History")
    print("3. Exit")
    user_choice = input("Choose an option: ")
    if user_choice == '1':
        functions.add_workout(data)
    elif user_choice == '2':
        functions.view_history(data)
    elif user_choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")



