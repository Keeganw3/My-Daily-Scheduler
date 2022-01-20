def add_to_day_planner():
    """
    Add options to the day planner.
    """
    while True:
        today = []
        print("Pick one number from 1-7 to select the option you want.")
        num = input("Enter your data here:")
        print(f"The option selected was {num}")
        validate_data(num)
        if int(num) == 1:
            today.append("Eat lunch")
        elif int(num) == 2:
            today.append("Go for a run")
        elif int(num) == 3:
            today.append("Walk your pet")
        elif int(num) == 4:
            today.append("Read a book")
        elif int(num) == 5:
            #function to display more options called
            print("Show more options")
        elif int(num) == 6:
            #Function to make an option called
            print("Make your own option")
        else:
            #function to exit day planner called
            print("Exit day planner")
        
        print(today)
        return False
    
    return today

def validate_data(values):
    """
    The try: converts all strings into integers.
    Makes an error if strings cannot be converted into int.
    """
    try:
        if int(values) >= 8 or int(values) <= 0:
            raise ValueError(
                f"A value from 1-5 is required, you provided {int(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def main():
    """
    Runs all functions in the program.
    """
    planned_day = add_to_day_planner()

print("Welcome! This is a Day Planner!")
print("Below are some suggestions for what you may want to do today.")
print("You can also make your own suggestions!")
print("Once you have 3 items in your day planner you will be asked if you're finished.")
print("If you say yes, your list will be shown to you.")
print("Otherwise, you will be able to add more to the day planner.")

main()