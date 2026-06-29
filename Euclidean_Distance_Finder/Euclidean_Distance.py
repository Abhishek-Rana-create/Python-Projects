# Prompt user to enter coordinates.
# Basic Error-handaling for non-numeric input.
def get_input(point):
    while True:
        try:
            x = float(input("Enter the x coordinate of {point} point: "))
            y = float(input("Enter the y coordinate of {point} point: "))
            return (x, y)
        except: ValueError
        print("Invalid Values. Please enter valid numeric values")

# Display Coordinates provided by the user.
# Prompt User to confirm Value by Y|N
def display_inputs(point_a, point_b):
    print(f"You entered {point_a} as one coordinate and {point_b} as another coordinate.")
    _ = input("Confirm Your answer by typing Y or N: ")
    if _.lower == str("y"):
        return True
    else:
        get_input()


