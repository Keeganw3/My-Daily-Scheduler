def daily_planner():
    """
    Add options to the day planner.
    """
    today = []
    print("Pick one number from 1-7 to select the option you want.")
    while True:
        if len(today) >= 3:
            print("Would you like to exit the daily planner?")
            user_input = input("Hit 'y' for yes and 'n' for no:")
            if user_input == 'y':
                print("Exiting daily planner...")
                return today
            elif user_input == 'n':
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
        print("7. Exit daily planner.")

        num = int(input("Enter the number here: "))
        print(f"The option selected was {num}")
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
            today.append(create_option())
        elif int(num) == 7:
            print("Exiting daily planner...")
            return today
        else:
            validate_input(num)
    return today


def validate_input(values):
    """
    The try: converts all strings into integers.
    Makes an error if strings cannot be converted into int.
    """
    while True:
        try:
            if values < 8 or values > 0:
                raise ValueError(
                    f"A value from 1-7 is required, you provided {int(values)}"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return True

        return True


def create_option():
    print("Type in your option below!")
    print("If this was a mistake type exit.")
    print("to return to previous options")
    user_made_option = input("")
    if user_made_option == "exit":
        pass
    else:
        return user_made_option


def other_options():
    """
    Gives the user extra options to select.
    """
    print("Here are some additional options:")
    print("1. Eat dinner")
    print("2. Schedule a meeting")
    print("3. Meet up with friends")
    print("4. Do homework")
    print("5. Show more options")
    print("6. Create new option")
    print("7. Exit daily planner.")
    num = int(input("Enter the number here: "))
    print(f"The option selected was {num}")
    if int(num) == 1:
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
    else:
        validate_input(num)


def main():
    """
    Runs all functions in the program.
    """
    plans = daily_planner()
    print(f"Here are your plans for the day: {plans}")
    print("I hope you enjoyed!")


print("Welcome! This is a Day Planner!")
print("Below are suggestions for what you may want to do.")
print("You can also make your own suggestions!")
print("When 3 items are in your day planner you will be asked if you're done.")
print("If you say yes, your list will be shown to you.")
print("Otherwise, you will be able to add more to the day planner.")
start = input("Hit Enter when you're ready to start the daily planner!")

main()
