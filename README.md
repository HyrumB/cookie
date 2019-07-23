# cookie

The goal of this project is to learn how to create and implement a programming language.

## Basic syntax

First of all we need to be able to assign a literal to a variable.
v = l;

Next we need to be able to create a function and assign it to a variable.
v = func {
  [statements]
  ...
}

Finally we need to be able to call a function.
v = f();

We will start out with only integers being valid literals.

Variables being any set of lowercase characters, plus the underscore, ie: [a-z_]+

And we will have some built in functions:
- add()
- print()

In this language, all variables are of a global scope, and nothing is ever freed,
although it can be re-used.

By convention parameters are the variables _1, _2, etc.

## Examples

Example Program:
```
_1 = 3;
_2 = 4;
sum = add()
_1 = sum
_ = print()
```

Example Ouput:
```
7
```
