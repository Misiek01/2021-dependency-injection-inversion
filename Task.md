DI - motivation.
Task 1.
Write two unit tests using pytest, that will verify the Order class initialization and set status.

Task 2.

Write three unit tests using pytest, that will verify Authorizer_SMS class.
https://www.w3schools.com/python/ref_string_isdecimal.asp

Explore `unittest.mock.patch`.

Task 2 b.
Write function that returns the dict with key `ids` and value list of numbers.
Call it `api_get_data_from_db`.

Write a class `OrderInterface` that implements a method `get_ids` which is using `api_get_data_from_db`.

Write a test for `get_ids` function and patch the output from `api_get_data_from_db`.

(Patch as decorator vs context manager)[https://realpython.com/python-mock-library/#patch-as-a-decorator]

Do the same using `Context Manager`.
Change return value during execution of the test.
Task 3.
How to test PaymentProcessor if authorizer is defined in the pay method.
Dependency Injection.