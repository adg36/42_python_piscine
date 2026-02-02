#!/usr/bin/env python3

import math


def ft_coordinate_system() -> None:
    pos_a = (0, 0, 0)
    pos_b = (10, 20, 5)

    print(f"Position created: {pos_b}")
    print_distance(pos_a, pos_b)

    good_coordinates = "3,4,0"
    bad_coordinates = "abc,def,ghi"

    print(f'Parsing coordinates: "{good_coordinates}"')
    pos_c = parse_coordinates(good_coordinates)
    print(f"Parsed position: {pos_c}")
    print_distance(pos_a, pos_c)
    print(f'Parsing invalid coordinates: "{bad_coordinates}"')
    try:
        parse_coordinates(bad_coordinates)
    except ValueError as e:
        print("Error parsing coordinates: ", e,
              f"\nError details - Type: ValueError, Args: {e.args}\n")
    print("Unpacking demonstration:")
    (x, y, z) = pos_c
    print(f"Player at x={x}, y={y}, z={z}\n"
          f"Coordinates: X={x}, Y={y}, Z={z}")


def parse_coordinates(coordinates: str) -> tuple:
    try:
        x_str, y_str, z_str = coordinates.split(",")
        x = int(x_str)
        y = int(y_str)
        z = int(z_str)
        position = tuple((x, y, z))
    except ValueError:
        raise
    return position


def print_distance(pos_a: tuple, pos_b: tuple) -> None:
    distance = math.sqrt((pos_b[0] - pos_a[0])**2 +
                         (pos_b[1] - pos_a[1])**2 + (pos_b[2] - pos_a[2])**2)
    print(f"Distance between {pos_a} and {pos_b}: {distance:.2f}\n")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    ft_coordinate_system()


if __name__ == "__main__":
    main()
