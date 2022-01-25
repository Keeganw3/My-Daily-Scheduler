def daily_planner():
    """
    Allows user to add options to the day planner. These options will be
    displayed to the user throughout their time using the code
    in a list and when they have exited the app.
    """
    today = []
    print("Pick a number from 1-7 to select the option you want.")
    while True:
        if len(today) >= 3:
            print("Would you like to exit the daily planner?")
            user_input = input(f"Hit 'y' for yes and 'n' for no:\n ")
            if user_input == "y":
                print("Exiting daily planner...")
                return today
            elif user_input == "n":
                pass
            else:
                print("'y' or 'n' wasn't selected. Please pick one.")
                continue

        print("1. Eat lunch")
        print("2. Go for a run")
        print("3. Walk your pet")
        print("4. Read a book")
        print("5. Show more options")
        print("6. Create new option")
        print(f"7. Exit daily planner.\n")
        
        try:
            num = int(input(f"Enter the number here:\n "))
            print(f"The option selected was {num}")
        except ValueError:
            print("Invalid you didn't enter a number.")
            input("Hit Enter to return to the main menu")
            continue            

        if int(num) == 1:
            today.append("Eat lunch")
            print(today)
        elif int(num) == 2:
            today.append("Go for a run")
            print(today)
        elif int(num) == 3:
            today.append("Walk your pet")
            print(today)
        elif int(num) == 4:
            today.append("Read a book")
            print(today)
        elif int(num) == 5:
            print("Show more options")
            today.append(other_options())
        elif int(num) == 6:
            print("Make your own option")
            if create_option() == "exit":
                continue
            else:
                today.append(create_option())
        elif int(num) == 7:
            print("Exiting daily planner...")
            return today
    return today


def create_option():
    """
    Allows the user to make their own option
    for the daily planner.
    """
    print("Type in your option below!")
    print("If this was a mistake type 'exit'.")
    print("to return to previous options")
    user_made_option = input(f"")
    return user_made_option


def main():
    """
    Runs all functions in the program.
    """
    plans = daily_planner()
    print(f"Here are your plans for the day: {plans}")
    print("I hope you enjoyed!")


if __name__:
    print("Welcome! This is a Daliy Planner!")
    print("Below are some suggestions for what you may want to do today.")
    print("You can also make your own suggestions!")
    print("When 3 tasks are in your day planner you will be asked if you're done.")
    print("If you say yes, your list will be shown to you.")
    print(f"Otherwise, you will be able to add more to the day planner.\n")
    input(f"Hit Enter when you're ready to start the daily planner!\n")
    main()

