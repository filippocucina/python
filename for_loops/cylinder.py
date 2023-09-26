import math, sys


def cylinder_volume(radius, height) -> int:
    return (math.pi * math.pow(radius, 2) * height)
    

def cylinder_area(radius) -> int:
    return (math.pi * math.pow(radius, 2))


def cylinder_lateral_area(radius, height) -> int:
    return (2 * math.pi * radius * height)

   
def cylinder_total_area(radius) -> int:
    return (2 * math.pi * math.pow(radius, 2))


def main() -> None:
    print("The cylinder's volume value is: " + str(cylinder_volume(5, 9)))
    print("The cylinder's area value is: " + str(cylinder_area(5)))
    print("The cylinder's lateral area is: " + str(cylinder_lateral_area(5, 9)))
    print("The cylinder's total area is: " + str(cylinder_total_area(5)))


if __name__ == "__main__":
    main()

