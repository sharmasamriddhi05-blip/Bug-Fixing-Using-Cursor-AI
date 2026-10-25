"""
Number and cart helper functions  -  FIXED VERSION.

Same functions as buggy_code.py, with all 6 bugs corrected.
Each fix is marked with a comment that starts with "FIX".
"""


def calculate_average(numbers):
    """Return the average of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot find the average of an empty list.")
    # FIX 1: divide by the real count, not count + 1
    return sum(numbers) / len(numbers)


def find_largest(numbers):
    """Return the largest number in a list."""
    if not numbers:
        raise ValueError("Cannot find the largest of an empty list.")
    # FIX 2: start from the first item, not 0, so all-negative lists work
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest


def count_even(numbers):
    """Return how many numbers in the list are even."""
    count = 0
    for n in numbers:
        # FIX 3: even numbers leave remainder 0 (the bug counted odd numbers)
        if n % 2 == 0:
            count += 1
    return count


def sum_up_to(n):
    """Return 1 + 2 + 3 + ... + n."""
    total = 0
    # FIX 4: range stops BEFORE the end value, so use n + 1 to include n
    for i in range(1, n + 1):
        total += i
    return total


def add_to_list(item, items=None):
    """Add an item to a list and return the list (a new list if none is given)."""
    # FIX 5: a default value of [] is created only once and shared by every call.
    # Use None and create a fresh list each time instead.
    if items is None:
        items = []
    items.append(item)
    return items


def build_message(name, total):
    """Return a message such as: Hello Riya, your total is 250"""
    # FIX 6: a string cannot be joined to a number with +, so use an f-string
    return f"Hello {name}, your total is {total}"


def main():
    print("Average of [10, 20, 30]:", calculate_average([10, 20, 30]))
    print("Largest of [-5, -2, -9]:", find_largest([-5, -2, -9]))
    print("Even numbers in [1, 2, 3, 4, 5]:", count_even([1, 2, 3, 4, 5]))
    print("Sum of 1 to 5:", sum_up_to(5))
    print("First list:", add_to_list("apple"))
    print("Second list:", add_to_list("banana"))
    print(build_message("Riya", 250))


if __name__ == "__main__":
    main()
