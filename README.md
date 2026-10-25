# Bug Fixing Project

I found and corrected 6 bugs in a buggy Python program, using an AI assistant to help
me understand each error. Each bug was found by comparing the program's output with the
answer I expected, then fixed and re-tested.

## Files

| File | What it is |
|------|------------|
| `buggy_code.py` | The original program with 6 bugs (before) |
| `fixed_code.py` | The corrected program, each fix marked with a `FIX` comment (after) |
| `run_tests.py` | A small test runner that shows which tests pass or fail |

## The 6 bugs

| # | Function | Bug | Wrong result | Fix |
|---|----------|-----|--------------|-----|
| 1 | `calculate_average` | Divided by `len + 1` instead of `len` | Average of 10, 20, 30 gave 15.0 instead of 20.0 | Divide by `len(numbers)` |
| 2 | `find_largest` | Started the search at `0` | Largest of -5, -2, -9 gave 0 instead of -2 | Start from the first item in the list |
| 3 | `count_even` | Checked `n % 2 == 1`, which counts odd numbers | Even count of 1 to 5 gave 3 instead of 2 (it counted odd numbers) | Check `n % 2 == 0` |
| 4 | `sum_up_to` | `range(1, n)` stops before `n` (off-by-one) | Sum of 1 to 5 gave 10 instead of 15 | Use `range(1, n + 1)` |
| 5 | `add_to_list` | Default argument `items=[]` is shared between calls | Second call returned both items | Use `items=None` and create a new list inside |
| 6 | `build_message` | Joined a string and a number with `+` | Crash: `TypeError` | Use an f-string |

## How to run

```
python buggy_code.py
python fixed_code.py
python run_tests.py buggy_code
python run_tests.py fixed_code
```

(On some systems use `python3` instead of `python`.)

The buggy file ends with an error on purpose. The tests show 0 of 6 passing for the buggy
version and 6 of 6 passing for the fixed version.

## What I learned

- Off-by-one mistakes are very common with `range`
- Starting a "largest" search at 0 fails for negative numbers
- A mutable default argument like `[]` is created only once and reused
- Reading the error message tells you the type of bug and the line to look at
- Writing a test with the expected answer is the fastest way to prove a bug is fixed

## Technologies

Python, GitHub

## Author

YOUR NAME
