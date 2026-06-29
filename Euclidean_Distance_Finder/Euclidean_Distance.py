def main():
    # ask user for coordinates of two points of First point
    x1, y1 = float(input("Enter x coordinate of first point: ")), float(input("Enter y coordinate of first point: "))

    # ask user for coordinates of two points of Second point
    x2, y2 = (float(input("Enter x coordinate of second point: ")), float(input("Enter y coordinate of second point: ")))

    a = (x1, y1)
    b = (x2, y2)

    return a, b
a, b = main()


def value_printer(a, b):
    print(f"first point coordinates are: ",{a})
    print(f"second point coordinates are: ",{b})
value_printer(a, b)

def Euclidean_Distance_operator(a, b):
    print(f"The distance between these two points is: ", ({b[0]-a[0]}) + ({b[1]-a[1]}), "units, as calculated from second point to first point.")
Euclidean_Distance_operator(a, b)


main()