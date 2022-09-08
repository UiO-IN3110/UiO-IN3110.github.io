---
title: "Assignment 2: Basic Python Programming"
layout: page
---

Maximum score: 15 points + 2 bonus points.

Your solutions to this assignment should be committed to the directory `assignment2` in your GitHub repository.

The assignment is broken into five tasks with one bonus task. The tasks are ordered so that you can develop the code incrementally, by first implementing 1d arrays and then 2d arrays. The bonus task is to implement n-d arrays.

The assignment requires knowledge of python types, functions, classes, unit tests, and exceptions.

**Tip:** If a task asks for something that has not yet been covered in class, you can make a comment saying e.g. `# TODO: Raise TypeError` and return at a later point.

## Errata

- The phrase "class variable" was previously used to describe "instance attributes" (i.e. assigning members (`self.x = x`) on your Array instance in `__init__`)
- Task 3 suggested returning NotImplemented for arithmetic methods with arrays of mismatched shapes.
  This will not be penalized, but raising an informative ValueError about the shape mismatch is more appropriate.

## Introduction

In this assignment you are going to implement a class `Array` in python. Arrays are data structures that represent a grid of values. These structures allow for storing a single data type - which makes them homogeneous. They are not only pretty neat, but also the most frequently used data structure in data science. Thus it is well worth spending some time on them.

For our implementation, the goal is to define a class `Array` that can
be used as follows:

```python
shape = (4,)
# define my_array
my_array = Array(shape, 2, 3, 1, 0)
# __getitem__ should be implemented correctly.
assert my_array[2] == 1
# Printing the array prints the array values nicely.
# For example: [2, 3, 1, 0]
print(my_array)
```

At this point you should take a look at [array_class.py][] and [test_array.py][] to see which methods and tests we are going to implement.

[array_class.py]: code/array_class.py
[test_array.py]: code/test_array.py

To get started, make an `assignment2` folder in your repo and download those two files into it.

Your repo should look like:

- `assignment1/...`
- `assignment2/array_class.py` ([source][array_class.py])
- `assignment2/test_array.py` ([source][test_array.py])

We will be working in this `assignment2` directory.

_Hint: now might be a good time to make a commit. That way you can easily see what code is yours,
and what came from the starter files._

## Important information

A key component of this course is teaching good code practice.

Your assignment is expected to

- contain a `README.md` with information on how to run your scripts,
- contain [unit tests](https://nbviewer.org/github/UiO-IN3110/UiO-IN3110.github.io/blob/HEAD/lectures/03-python-part-2/Testing.ipynb) with good code coverage,
- be well documented with [Google style docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

We will run unit tests (our own and the ones you write) when grading. For this reason it is **important that the names of methods and tests match what is specified in the assignment**.

Even though you get to enjoy implementing an `Array` class yourself you are free to look at the implementation of arrays in `NumPy`. However, should _not_ use `numpy.array` or `numpy.reshape` or Pythons own `array` class to solve this assignment.

## Implement the Array Class (6 points)

**Task 1:** Implement the Array class so that 1D array can be instantiated by `Array(shape, 1, 2, ..., n)`, and perform type checks on the arguments (1 point)

Here, _shape_ is a tuple of integers and refers to the dimensionality of the array. Therefore, _shape_ refers to the
"rows" and "columns" of the array, e.g. _shape(rows, columns)_.

A 1D array can be defined with shape (4,), that is, 4 elements in the first (and only) dimension.

```python
a = Array((4,), 1, 2, 3, 4)
```

The values should be stored as an instance attribute in a python list.

The arrays you create should be homogeneous, meaning all elements have
the same datatype. You only need to consider numeric types. There are
three distinct numeric types: integers, floating point numbers, and
complex numbers. In addition, booleans are a subtype of integers.

We will only consider the types integers, floats and booleans. If a combination of integers, floats and booleans are given, you should raise an informative `ValueError`.

Additionally, if _shape_ or _values_ do not have the right type, you should raise an informative `TypeError`. _shape_ should be of type tuple, and _values_ should consists of either ints, floats or booleans.

**Task 2:** Implement the `__getitem__()` method, to index the array (1 point)

**Task 3:** Implement the methods outlined in the `array_class.py` template for 1D arrays. (4 points)

The mathematical methods, `__add__`, `__sub__`,`__mul__`,
`__radd__`, `__rsub__`, `__rmul__`, `min_element` and `mean_element` __only need to be implemented for arrays containing ints and floats__. If these methods are called for a boolean array you can return `NotImplemented`.
For addition, subtraction, and multiplication you want to check if the argument is a scalar or an Array with the same shape.
If it is another type, you can return `NotImplemented`.
If it is an Array and the shape does not match,
raising an informative ValueError is appropriate.

**EDIT:** earlier forms of the assignment suggested returning `NotImplemented` for a shape mismatch. This will be accepted, but is not a best practice.

The methods `__radd__`, `__rsub__` and `__rmul__` are called to
implement the arithmetic operations `__add__`, `__sub__`,`__mul__` with
swapped operands. The `r methods` are called if the left (first)
operand does not support the operation provided and the operands are of
different type. For example, imagine we have an array

```python
array1 = Array((6,), 1, 2, 3, 4, 5, 6)
```

and want to evaluate `10 + array1`, where array1 is an instance of our
`Array` class, which has a `__radd__()` method. Python first calls
`10_̇_add__(array1)`. Since 10 (int or float) does not support the
instance of the `Array` class, `10_̇_add__(array1)` it returns
`NotImplemented`. The r-method `array1_̇_radd__(10)` is then called.

```python
array1 = Array((6,), 1, 2, 3, 4, 5, 6)
i = 10
i.__add__(array1) # Returns NotImplemented

array1.__radd__(i) # Returns Array((6,), 11, 12, 13, 14, 15, 16)
```

Another explanation can be found [here](https://stackoverflow.com/questions/9126766/addition-between-classes-using-radd-method/38196153).

Do not use `NotImplemented` for other normal methods (such as
`min_element`). For `min_element`, we don't require error handling, but
you can raise a `ValueError` or `TypeError`.

Read the [outline we provided](code/array_class.py) of the array class carefully, as we
provided additional information on the different methods to be
implemented.

## Unit Tests for 1D Arrays (4 points)

Let's dive into the "real world" of development. Then it is good practice to write tests for each aspect of the code.

If, for instance, you want to write an addition function `plus(a, b)`,
you would expect that 2 and 2 becomes 4. To check that the function
actually does that, you can formalize it as a unit test:

```python
def test_two_plus_two():
    assert plus(2, 2) == 4
```

A test should have a name starting with `test_`, and raise an `AssertionError` if the test fails (this is what the `assert`
statement does). The test should always test the specific task your
function or class is performing. Furthermore, the test should always
test the same task/functionality, i.e. generating something random in a test is usually a bad idea since you might end up with tests that
_sometimes_ pass.

**Task 4:** Implement the following tests (4 points, 0.5 points each):

- 4.1. `test_str_1d()` to check that your print function returns a nice string.
- 4.2. `test_add_1d()` to check that adding to a 1d-array element-wise returns what it's supposed to.
- 4.3 `test_sub_1d()` to check that subtracting from a 1d-array element-wise returns what it's supposed to.
- 4.4 `test_mul_1d()` to check that multiplying a 1d-array element-wise by a factor or other 1-d array returns what it's supposed to.
- 4.5 `test_eq_1d()` to check that comparing arrays (by `==`) returns what it is supposed to - which should be a boolean.
- 4.6 `test_same_1d()` to check that comparing a 1d-array element-wise to another array through `is_equal` returns what it's supposed to - which should be a boolean array.
- 4.7 `test_smallest_1d()` to check that the element returned by `min_element` is the "smallest" one in the array.
- 4.8 `test_mean_1d()` to check that taking the mean of an array returns what it's supposed to.

The tests should live in a separate file named `test_array.py`. You will need to import the `Array`-class properly in order to run your tests.

**Note**: It is useful and common to use _pytest_ to run and make the tests. Among other things, pytest can be used to automatically call all tests. When running `pytest` in the terminal, pytest runs all functions starting with `test_` or ending with `_test`. See more [here](http://doc.pytest.org/en/latest/getting-started.html).

The tests should be written so that they exhibit _high coverage_, i.e. they should cover most of the use cases expected. For example `test_add_1d()` should test array addition for integers, floats and booleans, as well as the `__radd__()` function.

Docstrings are not needed for tests, but you may have a comment that describes what the method does in `test_array.py`. Good examples can be found [here](https://docs.pytest.org/en/6.2.x/getting-started.html#create-your-first-test).

## Adapt your implementation to work with 2D Arrays (3 points)

**Task 5:** Modify your Arrays implementation so that it works with 1D and 2D arrays (3 points)

The following code should be a valid way of
defining a 2D array with shape $(3, 2)$.

```python
# define my_array
my_array = Array((3, 2), 8, 3, 4, 1, 6, 1)
# accessing values should work as follows
assert my_array[1][0] == 4
```

Start with modifying your class constructor `__init__` to handle both 1D and 2D. The values should now be stored in _nested list_ (a list of list).

**Hint:** It can be a good idea to flatten the 2D array when performing element-wise operations. Then you do not need to handle the 1D and 2D case differently everywhere.

An inspiration for such a function is given below:

```python
def flat_array(self):
   """Flattens the N-dimensional array of values into a 1-dimensional array.
   Returns:
       list: flat list of array values.
   """
   flat_array = self._array
   for _ in range(len(self.shape[1:])):
       flat_array = list(chain(*flat_array))
   return flat_array
```

The function _chain_ can be imported from itertools with `from itertools import chain`. If you encounter a function or library you haven't heard of before, you should google the name and read its documentation. In this case, you can find it [here](https://docs.python.org/3/library/itertools.html#itertools.chain).

**Note**: Instead of calling `flat_array()` every time you do an operation on the flattened array, you can save what it returns as an attribute. This way you won't have to compute the flattened array each time you index something, which would be inefficient.

## Additional tests for 2D Arrays (2 point)

**Task 6:** Add the following tests for 2-dimensional arrays, i.e. arrays with shape $(n, m)$ where $n$ and $m$ are integers (2 points, 0.5 points each)

- 6.1 `test_add_2d()` to check that adding to a 2d-array element-wise returns what it's supposed to.
- 6.2 `test_mult_2d()` to check that multiplying a 2d-array element-wise returns what it's supposed to.
- 6.3 `test_same_2d()` to check that comparing a 2d-array element-wise to another array through `is_equal` returns what it's supposed to.
- 6.4 `test_mean_2d()` to check that taking the mean of an array returns what it's supposed to

Docstrings are not needed for tests, but you should have a comment
that describes what the method does in `test_array.py` Good examples
can be found [here](https://docs.pytest.org/en/6.2.x/getting-started.html#create-your-first-test).

## n-dimensional Arrays (2 Bonus Points)

**Bonus task 1:** Make all the methods implemented in Task 3 work with n-dimensional arrays. Make sure not to break your previous tests. (2 points)

## Checklist before submitting

In order for your code to be automatically gradable, please note:

- [ ] Assignment is in your `assignment2` folder
- [ ] You should not import `numpy.array` or `numpy.reshape` or Pythons own `array` class
- [ ] You should implement the `Array` methods with the method names, arguments and return arguments given in `array_class.py`
- [ ] You should implement the unit tests in `test_array.py` with the given function names
- [ ] Don't forget to push! _Committing is not turning it in_, make sure your work can be seen at https://github.uio.no/IN3110/in3110-yourname

## Extra: Some comments about computational efficiency in python

The underlying data structure for our array-class in this assignment is the python-list, which is not homogenous and _can_ contain multiple types. This is not the case with a lot of lower level programming languages, like Java, C and C++, where the basic array only can contain one type. Being able to have lists that can contain multiple types can be very convenient in higher-level programming, but it sacrifices computationally efficiency. Arrays and loops in C are _much_ faster than in python, and since we heavily rely on python loops and lists in this assignment, you should expect it to perform poorly in terms of speed.

### But if python lists and loops are so slow, why are so many important libraries written in python?

Even though some of the most used scientific programming libraries, like NumPy, Pandas, Scikit-learn, Pytorch and TensorFlow, can be used in python, they actually mostly run in C or C++. When you for example multiply two big numpy-arrays in python, the python-numpy code actually executes Fortran code! This way, all of the loops can happen efficiently on a lower level, while the code can be called easily and user-friendly in python. Win-Win!

Therefore, you should probably use well-known libraries instead of your own data structures when writing important code. These libraries often have other major speed-ups as well, such as parallelization, cache-optimization, efficient choice of algorithms and data structures depending on the input, and much more. You can often expect about a 100x times speed increase when using C loops or numpy instead of python. For specific tasks, like altering pixels in an image, specialized software like numpy may easily give a 1 000 to 1 000 000x speed increase over plain python code (!).
