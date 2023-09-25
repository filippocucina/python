import math


def triangle_perimeter(a, b, c) -> int:
    return a + b + c


def triangle_area(a, b, c) -> int:
    s = (a + b + c) / 2 #semiperimeter
    diference1 = s - a
    diference2 = s - b
    diference3 = s - c
    heron_formula = s * diference1 * diference2 * diference3

    return math.floor(math.sqrt(heron_formula))
    

def main() -> None:
    print(triangle_perimeter(3, 4, 5))
    print(triangle_area(3, 4, 5))

if __name__ == "__main__":
    main()
