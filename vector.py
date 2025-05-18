from dataclasses import dataclass
import math

Number = int | float


@dataclass(frozen=True)
class Vector2D:
    """
    A class to represent a 2D vector with x and y components.

    Attributes:
        x (float): The x-coordinate of the vector.
        y (float): The y-coordinate of the vector.
    """

    x: float
    y: float

    def __repr__(self) -> str:
        """
        Return a string representation of the vector.

        Returns:
            str: A string in the format 'Vector2D(x=value, y=value)'.
        """
        return f"Vector2D(x={self.x}, y={self.y})"

    def __add__(self, other: "Vector2D") -> "Vector2D":
        """
        Add two vectors component-wise.

        Args:
            other (Vector2D): The vector to add.

        Returns:
            Vector2D: The resulting vector after addition.
        """
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        """
        Subtract another vector from this vector component-wise.

        Args:
            other (Vector2D): The vector to subtract.

        Returns:
            Vector2D: The resulting vector after subtraction.
        """
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: Number) -> "Vector2D":
        """
        Multiply the vector by a scalar.

        Args:
            scalar (Number): The scalar to multiply with.

        Returns:
            Vector2D: The resulting vector after multiplication.
        """
        return Vector2D(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def __truediv__(self, scalar: Number) -> "Vector2D":
        """
        Divide the vector by a scalar.

        Args:
            scalar (Number): The scalar to divide by.

        Returns:
            Vector2D: The resulting vector after division.

        Raises:
            ValueError: If the scalar is zero.
        """
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector2D(self.x / scalar, self.y / scalar)

    def __neg__(self) -> "Vector2D":
        """
        Negate the vector (invert its direction).

        Returns:
            Vector2D: The negated vector.
        """
        return Vector2D(-self.x, -self.y)

    def __abs__(self) -> float:
        """
        Compute the magnitude (length) of the vector.

        Returns:
            float: The magnitude of the vector.
        """
        return self.magnitude()

    def __eq__(self, other) -> bool:
        """
        Check if two vectors are approximately equal.

        Args:
            other (Vector2D): The vector to compare with.

        Returns:
            bool: True if the vectors are approximately equal, False otherwise.
        """
        if not isinstance(other, Vector2D):
            return NotImplemented
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

    def __hash__(self) -> int:
        """
        Compute a hash value for the vector.

        Returns:
            int: The hash value of the vector.
        """
        return hash((round(self.x, 10), round(self.y, 10)))

    @classmethod
    def euler(cls, magnitude: float, angle: float) -> "Vector2D":
        """
        Create a vector from magnitude and angle using Euler's formula.

        Args:
            magnitude (float): The magnitude of the vector.
            angle (float): The angle of the vector in radians.

        Returns:
            Vector2D: The resulting vector.
        """
        return cls(magnitude * math.cos(angle), magnitude * math.sin(angle))

    def conjugate(self) -> "Vector2D":
        """
        Compute the conjugate of the vector (invert the y-component).

        Returns:
            Vector2D: The conjugated vector.
        """
        return Vector2D(self.x, -self.y)

    def magnitude(self) -> float:
        """
        Compute the magnitude (length) of the vector.

        Returns:
            float: The magnitude of the vector.
        """
        return math.hypot(self.x, self.y)

    def argument(self) -> float:
        """
        Compute the argument (angle) of the vector in radians.

        Returns:
            float: The angle of the vector in radians.

        Raises:
            ValueError: If the vector is a zero vector.
        """
        if self.x == 0 and self.y == 0:
            raise ValueError("Cannot compute argument of a zero vector")
        return math.atan2(self.y, self.x)

    def normalize(self) -> "Vector2D":
        """
        Normalize the vector to have a magnitude of 1.

        Returns:
            Vector2D: The normalized vector.

        Raises:
            ValueError: If the vector is a zero vector.
        """
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return self / mag

    def dot(self, other: "Vector2D") -> float:
        """
        Compute the dot product of this vector and another vector.

        Args:
            other (Vector2D): The vector to compute the dot product with.

        Returns:
            float: The dot product of the two vectors.
        """
        return self.x * other.x + self.y * other.y

    def cross(self, other: "Vector2D") -> float:
        """
        Compute the z-component of the 3D cross product of this vector and another vector.

        Args:
            other (Vector2D): The vector to compute the cross product with.

        Returns:
            float: The z-component of the cross product.
        """
        return self.x * other.y - self.y * other.x
