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


