## Pytest Intro

[Pytest Intro](https://realpython.com/pytest-python-testing/#how-to-install-pytest)
Install pytest.

## Task 1 Write test asserting product of two numbers is equal the fixture value.


## How to run pytest in VS Code

[Pytest in VS Code](https://pytest-with-eric.com/introduction/how-to-run-pytest-in-vscode/)

## Patch
Go to `utils.py` (implementation of Task 2b). Explore the code.

## Task 2 Write test for get_ids method using patch.
[Patch](https://realpython.com/python-mock-library/)
Patching will be used for the function `utils.api_get_data_from_db` to return static value.


## Dependency in object oriented programming
Object that class has a direct relationship with.
Class and directed object type are coupled.
Class could depend on another class, because it has an attribute of that type
or becauce object of that type is passed as a parameter to method,
or because the class inherits.
Inheritance introduce the coupling that is hard to remove.
`Composition is always a better choice then inheritance`.
[Composition and Inheritance](https://realpython.com/inheritance-composition-python/#composition-in-python)

## Dependency Injection
`Dependency Injection` is a design pattern.
The idea is that,
if the class uses an object of the certain type
we are not making that class responsible for that object.
`Because it shifts the responsibility of creating to another class`
`dependency injection` is an inversion of control technique.

Big advanatge of dependency injeciton is that your code is much easier to test.

## Dependency inversion
`Dependency inversion` is a prinicple in `SOLID` design principles.
Decoupled concrete classes uses abstractions, abstract classes, interfaces etc.

Because you need a class in order to construct the object.
This also means that `dependecy inversion` is possible when you
separate creation from use.
Without `Dependency Injection` there is no `Dependency Inversion`.



## before
Go to file `before.py`.

## Task 3 Create automated tests for classes in file before.py

It is hard to test `PaymentProcessor` for success and fail,
because it creates authoriser object, calls methods and
checks wheater is authorized or not.

Problem is that
the pay method is responsible for creating objects
which means we can NOT create it in test,
sets to true and pass to the pay method.

Unit test has a mock method that allows you
to mock object that are used in functions
and replace that objects in those functions.
IT IS HARD.

That's where `DEPENDENCY INJECTION` pattern comes to play.

Introduce dependency injection to
ehnace testability and later dependecy inversion.

We can introduce dependency in
`parameter of the method` or
`initializer in the class`.

The advantage of the second is that we can use it in different places.

Remove from `pay` function, the generation of sms,
because it is not its responsibility.
Go to `with_dep_inj_test.py`.

## Task 4 Write test for PaymentProcessor class.

`Suggestion`:
Test how the class is created and init.

## Generate the coverage report
## Task 5: Check it out
https://coverage.readthedocs.io/en/7.2.7/
`coverage html`
`coverage run test.py`
`coverage html`
check `index.html` in html reader.

## Dependency Inversion
## Task 6: Explore the file final.py
We create a layer between that allows us to separate
the payment process from
authorization
much clenanly.

Beacuse the payment processor only calls two methods it does not need to
know we are dealing with `AuthorizerSMS`.
We can give him an abstract class, that will have the abstract methods it needs.

## Coverage issue due to abstract class
Beacuse we added this abstract class, we introduced two
abstract methods which are not tested, which is true.
On the other habd is useless to test those methods because they are abstract.

Coeverage ingores the method to test
if we replace `pass` with doctring.

## Dependency Inversion
Is important, allows to separate Authorizer and Payment Processor,
do not need to know much about them selfs.
