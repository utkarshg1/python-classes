# Vector2D Class

The `Vector2D` class is a Python implementation of a 2D vector with various mathematical operations and utilities. It is designed to be immutable and provides a wide range of methods for vector arithmetic, normalization, and more.

## Features

- **Vector Arithmetic**: Add, subtract, multiply, and divide vectors.
- **Magnitude and Normalization**: Compute the magnitude and normalize vectors.
- **Dot and Cross Products**: Perform dot and cross product operations.
- **Angle and Conjugate**: Compute the angle (argument) and conjugate of vectors.
- **Euler's Formula**: Create vectors using magnitude and angle.

## Class Definition

```python
@dataclass(frozen=True)
class Vector2D:
    x: float
    y: float
```

### Attributes

- `x` (float): The x-coordinate of the vector.
- `y` (float): The y-coordinate of the vector.

## Methods

### Arithmetic Operations

- `__add__(other: Vector2D) -> Vector2D`: Add two vectors.
- `__sub__(other: Vector2D) -> Vector2D`: Subtract one vector from another.
- `__mul__(scalar: Number) -> Vector2D`: Multiply the vector by a scalar.
- `__truediv__(scalar: Number) -> Vector2D`: Divide the vector by a scalar.

### Vector Properties

- `magnitude() -> float`: Compute the magnitude (length) of the vector.
- `normalize() -> Vector2D`: Normalize the vector to have a magnitude of 1.
- `argument() -> float`: Compute the angle of the vector in radians.

### Vector Operations

- `dot(other: Vector2D) -> float`: Compute the dot product of two vectors.
- `cross(other: Vector2D) -> float`: Compute the z-component of the 3D cross product.
- `conjugate() -> Vector2D`: Compute the conjugate of the vector.

### Utility Methods

- `euler(magnitude: float, angle: float) -> Vector2D`: Create a vector from magnitude and angle using Euler's formula.

## Example Usage

```python
from vector import Vector2D

# Create vectors
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

# Vector addition
v3 = v1 + v2
print(v3)  # Output: Vector2D(x=4, y=6)

# Magnitude
print(v1.magnitude())  # Output: 5.0

# Normalize
v4 = v1.normalize()
print(v4)  # Output: Vector2D(x=0.6, y=0.8)

# Dot product
dot_product = v1.dot(v2)
print(dot_product)  # Output: 11

# Cross product
cross_product = v1.cross(v2)
print(cross_product)  # Output: 2
```

## Error Handling

- Division by zero raises a `ValueError`.
- Normalizing a zero vector raises a `ValueError`.
- Computing the argument of a zero vector raises a `ValueError`.

## License

This project is licensed under the MIT License.
