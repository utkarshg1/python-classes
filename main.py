import math
from vector import Vector2D

vec1 = Vector2D(3, 4)
vec2 = Vector2D(1, 2)


def main():
    print("Vector 1:", vec1)
    print("Vector 2:", vec2)
    print("Magnitude of Vector 1:", vec1.magnitude())
    print("Argument of Vector 1:", vec1.argument())
    print("Magnitude of Vector 2:", vec2.magnitude())
    print("Argument of Vector 2:", vec2.argument())
    print("Normalization of Vector 1:", vec1.normalize())
    print("Normalization of Vector 2:", vec2.normalize())
    print("\n" + "=" * 50 + "\n")

    print("Addition:", vec1 + vec2)
    print("Subtraction:", vec1 - vec2)
    print("Multiplication by scalar:", vec1 * 2)
    print("Division by scalar:", vec1 / 2)
    print("Equality check:", vec1 == vec2)
    print("\n" + "=" * 50 + "\n")

    print("Dot product:", vec1.dot(vec2))
    print("Cross product:", vec1.cross(vec2))
    print("\n" + "=" * 50 + "\n")

    euler_vec = Vector2D.euler(5, math.pi / 3)
    print("Euler vector with magnitude 5 and angle pi/3:", euler_vec)


if __name__ == "__main__":
    main()
