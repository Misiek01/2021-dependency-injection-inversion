# Dependency in object oriented programming
Object that class has a direct relationship with.
Class and directed object type are coupled.
Class could depend on another class, because it has an attribute of that type
or becauce object of that type is passed as a parameter to method,
or because the class inherits.
Inheritance introduce the coupling that is hard to remove.
`Composition is always a better choice then inheritance`.

# Dependency Injection
`Dependency Injection` is a design pattern.
The idea is that, 
if the class uses an object of the certain type
we are not making that class responsible for that object.
`Because it shifts the responsibility of creating to another class`
`dependency injection` is an inversion of control technique.

Big advanatge of dependency injeciton is that your code is much easier to test.

# Dependency inversion 
`Dependency inversion` is a prinicple in `SOLID` design principles.
Decoupled concrete classes uses abstractions, abstract classes, interfaces etc.

Because you need a class in order to construct the object.
This also means that `dependecy inversion` is possible when you
separate creation from use.
Without `Dependency Injection` there is no `Dependency Inversion`.



# before-test

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
because it is not irs responsibility.

`Suggestion`:
Test how the class is created and init.

# Generate the coverage report
# TODO 
https://coverage.readthedocs.io/en/7.2.7/
`coverage html`
