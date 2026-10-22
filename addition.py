from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    print(f"Sum: {add(first_number, second_number)}")
