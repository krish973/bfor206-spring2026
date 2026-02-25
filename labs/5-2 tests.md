# BFOR 206 Lab 5-2: Tests

## Task Description

Create and test a function using Pytest. You will need to create
two scripts: `class_testing.py` and `tests/test_class_testing.py`.

In the `class_testing.py` file, create a function
named `string_checker.py` that takes two strings as arguments
and checks if the second string is a substring of the first.
The function should return `True` if the second string is a substring of the
first, and `False` otherwise.

In the `tests/test_class_testing.py` file, create a test function
named `test_string_checker` that tests the `string_checker`.

The test should have two cases, see the 
example in the `tests/test_class_testing.py`
file for reference.

## Testing

```bash
# run this in the terminal
python -m pytest 
```

If successful, the output should show that the tests passed.
If it fails it will show the cause of the error. An 
AssertionError means that the test failed because the expected output did not 
match the actual output. In other words, the function did not return 
what was expected.


### Alternate Testing Method

You may also use the integrated testing features in VSCode.

## Submission instructions

**Scripts that output Python errors will not be accepted!**

Run your script to show that the tests pass.

When you are finished, show the instructor:

1. The successful test run.
2. You testing code.
