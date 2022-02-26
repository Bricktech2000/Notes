# Optimizing a Function

see [[extremum]], [[classical-math-notation]]

> Practically, function optimization describes a class of problems for finding the input to a given function that results in the minimum or maximum output from the function. — machinelearningmastery.com

## method

1. [[calculating-a-derivative]] to find [[extremum]].
2. use second derivative test (see [[extremum]]) to determine type of extremum.
3. use the information above to maximize or minimize the output of the function

## example

maximize $f(x) = 600x - 2x^2$

1. $f'(x) = 600 - 4x$. $f'(x) = 0\ \text{for}\ x = 150$
2. $f''(x) = -4$, meaning this is a local maximum (see [[extremum]])
3. the function is maximized at $x = 150$, $f(150) = 45000$
