def daily_planner():
    """
    Allows user to add options to the day planner.
    These options will be displayed to the user
    throughout their time using the code in a
    list and when they have exited the app.
    """
    today = []
    print("Pick a number from 1-6 to select the option you want.")
    while True:
        if len(today) >= 3:
            print("Would you like to exit the daily planner?")
            user_input = input(f"Hit 'y' for yes and 'n' for no:\n")
            print("")
            if user_input.strip().lower() == "y":
                input(f"You are now leaving the daily planner:\n")
                print("Exiting daily planner...")
                return today
            elif user_input.strip().lower() == "n":
                input(f"You selected 'n' and will be returned to the main menu:\n")
                pass
            else:
                print("'y' or 'n' wasn't selected. Please pick one.")
                continue

        print("1. Eat lunch")
        print("2. Go for a run")
        print("3. Walk your pet")
        print("4. Read a book")
        print("5. Create new option")
        print(f"6. Exit daily planner.\n")

        try:
            num = int(input(f"Enter your number here:\n"))
        except ValueError:
            print("Invalid you didn't enter a number.")
            input("Hit Enter to return to the main menu.")
            continue

        if num == 1:
            today.append("Eat lunch")
            print(today)
            print("")
        elif num == 2:
            today.append("Go for a run")
            print(today)
            print("")
        elif num == 3:
            today.append("Walk your pet")
            print(today)
            print("")
        elif num == 4:
            today.append("Read a book")
            print(today)
            print("")
        elif num == 5:
            print("Make your own option")
            if create_option() == "exit":
                print(today)
                print("")
            else:
                today.append(create_option())
                print(today)
                print("")
        elif num == 6:
            print("Exiting daily planner...")
            return today
        else:
            print(f"Number out of range. Pick a number from 1-6.\n")
    return today


def create_option():
    """
    Allows the user to make their own option
    for the daily planner. This option is
    returned by the function.
    """
    print("Type in your option below!")
    print("If this was a mistake type 'exit'")
    print("to return to previous options.")
    user_made_option = input(f"\n")
    return user_made_option


def main():
    """
    Runs all functions in the program.
    """
    plans = daily_planner()
    print(f"Here are your plans for the day: {plans}")
    print("I hope you enjoyed!")


if __name__ == "__main__":
    print("Welcome! This is a Daily Scheduler!")
    print("Below are some suggestions for what you may want to do today.")
    print("You can also make your own suggestions!")
    print("You'll be asked if you're done when you've add 3 tasks.")
    print("If you say yes, your list of tasks will be shown to you.")
    print(f"Otherwise, you will be able to add more to the day planner.\n")
    input(f"Hit Enter when you're ready to start the daily planner!\n")
    main()
