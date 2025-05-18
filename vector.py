from dataclasses import dataclass
import math


Number = int | float


@dataclass(frozen=True)
class Vector2D:
    x: float
    y: float

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: Number) -> "Vector2D":
        return Vector2D(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def __truediv__(self, scalar: Number) -> "Vector2D":
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector2D(self.x / scalar, self.y / scalar)

    def __neg__(self) -> "Vector2D":
        return Vector2D(-self.x, -self.y)

    def __abs__(self) -> float:
        return self.magnitude()

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

    def __hash__(self) -> int:
        return hash((round(self.x, 10), round(self.y, 10)))

    @classmethod
    def euler(cls, magnitude: float, angle: float) -> "Vector2D":
        return cls(magnitude * math.cos(angle), magnitude * math.sin(angle))

    def conjugate(self) -> "Vector2D":
        return Vector2D(self.x, -self.y)

    def magnitude(self) -> float:
        return math.hypot(self.x, self.y)

    def argument(self) -> float:
        if self.x == 0 and self.y == 0:
            raise ValueError("Cannot compute argument of a zero vector")
        return math.atan2(self.y, self.x)

    def normalize(self) -> "Vector2D":
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return self / mag

    def dot(self, other: "Vector2D") -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other: "Vector2D") -> float:
        # Returns the z-component of the 3D cross product
        return self.x * other.y - self.y * other.x
