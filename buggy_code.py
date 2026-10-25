"""
Number and cart helper functions  -  BUGGY VERSION.

This file has 6 bugs on purpose. Run it, read the wrong output,
then compare with fixed_code.py to see how each bug was found and fixed.
"""


def calculate_average(numbers):
    """Return the average of a list of numbers."""
    return sum(numbers) / (len(numbers) + 1)


def find_largest(numbers):
    """Return the largest number in a list."""
    largest = 0
    for n in numbers:
        if n > largest:
            largest = n
    return largest


def count_even(numbers):
    """Return how many numbers in the list are even."""
    count = 0
    for n in numbers:
        if n % 2 == 1:
            count += 1
    return count


def sum_up_to(n):
    """Return 1 + 2 + 3 + ... + n."""
    total = 0
    for i in range(1, n):
        total += i
    return total


def add_to_list(item, items=[]):
    """Add an item to a list and return the list (a new list if none is given)."""
    items.append(item)
    return items


def build_message(name, total):
    """Return a message such as: Hello Riya, your total is 250"""
    return "Hello " + name + ", your total is " + total


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
