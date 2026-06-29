# Prompt user to enter coordinates.
def get_input(point):
    while True:
        try:
            x = float(input(f"Enter the x coordinate of the {point} point: "))
            y = float(input(f"Enter the y coordinate of the {point} point: "))
            return (x, y)
        except ValueError:
            print("Invalid values. Please enter numeric values.")


# Display coordinates and ask for confirmation.
def display_inputs(point_a, point_b):
    print(f"\nYou entered:")
    print(f"Point A = {point_a}")
    print(f"Point B = {point_b}")

    while True:
        choice = input("Confirm? (Y/N): ").strip().lower()

        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Please enter only Y or N.")


# Calculate Euclidean distance.
def calculator(point_a, point_b):
    dx = point_b[0] - point_a[0]
    dy = point_b[1] - point_a[1]
    return (dx**2 + dy**2) ** 0.5


# Main pipeline.
def main():
    while True:
        point_a = get_input("first")
        point_b = get_input("second")

        if display_inputs(point_a, point_b):
            break
        else:
            print("\nLet's enter the coordinates again.\n")

    distance = calculator(point_a, point_b)
    print(f"\nEuclidean Distance = {distance:.3f}")


if __name__ == "__main__":
    main()