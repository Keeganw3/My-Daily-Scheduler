def add_to_day_planner():
    """
    Add options to the day planner
    """
    while True:
        today = []
        print("Pick one number from 1-5 to select the option you want.")
        num = input("Enter your data here:")
        print(f"The option selected was {num}")
        validate_data(num)

        if validate_data(num):
            print('number is valid!')
            break

    return num

def validate_data(values):
    """
    The try: converts all strings into integers.
    Makes an error if strings cannot be converted into int.
    """
    try:
        if int(values) >= 6 or int(values) <= 0:
            raise ValueError(
                f"A value from 1-5 is required, you provided {int(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

#def main()

print("Welcome! This is a Day Planner!")
print("Below are some suggestions for what you may want to do today.")
print("You can also make your own suggestions!")
print("Once you have 3 items in your day planner you will be asked if you're finished.")
print("If you say yes, your list will be shown to you.")
print("Otherwise, you will be able to add more to the day planner.")
#main()
add_to_day_planner()