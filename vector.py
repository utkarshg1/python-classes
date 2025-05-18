import math


class Vector2D:

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector2D":
        return Vector2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: float) -> "Vector2D":
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector2D(self.x / scalar, self.y / scalar)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            raise TypeError(f"Cannot compare Vector2D with {type(other).__name__}")
        return self.x == other.x and self.y == other.y

    def __iter__(self):
        yield self.x
        yield self.y

    @classmethod
    def euler(cls, magnitude: float, angle: float) -> "Vector2D":
        return Vector2D(
            magnitude * math.cos(angle),
            magnitude * math.sin(angle),
        )

    def magnitude(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def argument(self) -> float:
        if self.x == 0 and self.y == 0:
            raise ValueError("Cannot compute argument of a zero vector")
        return math.atan2(self.y, self.x)

    def normalize(self) -> "Vector2D":
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector2D(self.x / mag, self.y / mag)

    def dot(self, other: "Vector2D") -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(
            self.y * other.x - self.x * other.y, self.x * other.y - self.y * other.x
        )
