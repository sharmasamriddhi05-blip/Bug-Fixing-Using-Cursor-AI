"""
Tiny test runner.

Each test checks one function against the answer we EXPECT.
Run it on either file to see which tests pass or fail:

    python run_tests.py buggy_code
    python run_tests.py fixed_code
"""

import importlib
import sys


def run_tests(module_name):
    code = importlib.import_module(module_name)

    # Each test is: (description, function to run, expected answer)
    tests = [
        ("average of [10, 20, 30] is 20",
         lambda: code.calculate_average([10, 20, 30]), 20),
        ("largest of [-5, -2, -9] is -2",
         lambda: code.find_largest([-5, -2, -9]), -2),
        ("even numbers in [1..5] is 2",
         lambda: code.count_even([1, 2, 3, 4, 5]), 2),
        ("sum of 1 to 5 is 15",
         lambda: code.sum_up_to(5), 15),
        ("second call to add_to_list gives only ['banana']",
         lambda: (code.add_to_list("apple"), code.add_to_list("banana"))[1], ["banana"]),
        ("message text is correct",
         lambda: code.build_message("Riya", 250), "Hello Riya, your total is 250"),
    ]

    passed = 0
    print(f"Testing {module_name}.py\n")
    for description, test, expected in tests:
        try:
            result = test()
        except Exception as error:      # the test crashed
            print(f"FAIL  {description}  ->  crashed: {type(error).__name__}: {error}")
            continue

        if result == expected:
            print(f"PASS  {description}")
            passed += 1
        else:
            print(f"FAIL  {description}  ->  got {result!r}, expected {expected!r}")

    print(f"\n{passed} of {len(tests)} tests passed.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_tests.py buggy_code   (or fixed_code)")
    else:
        run_tests(sys.argv[1])
