# Optimizing a Function

see [Extremum](Extremum%20b28f7c5907fb47adb037ca90b838c2db.md), [Classical Math Notation](Classical%20Math%20Notation%20eb53679093ce497baa118d7bfde14d6c.md)

> Practically, function optimization describes a class of problems for finding the input to a given function that results in the minimum or maximum output from the function. — machinelearningmastery.com
> 

## method

1. [Calculating a Derivative](Calculating%20a%20Derivative%208ee8cca8aa8f46749f2d88c898b8466d.md) to find [Extremum](Extremum%20b28f7c5907fb47adb037ca90b838c2db.md).
2. use second derivative test (see [Extremum](Extremum%20b28f7c5907fb47adb037ca90b838c2db.md)) to determine type of extremum.
3. use the information above to maximize or minimize the output of the function

## example

maximize $f(x) = 600x - 2x^2$

1. $f'(x) = 600 - 4x$. $f'(x) = 0\ \text{for}\ x = 150$
2. $f''(x) = -4$, meaning this is a local maximum (see [Extremum](Extremum%20b28f7c5907fb47adb037ca90b838c2db.md))
3. the function is maximized at $x = 150$, $f(150) = 45000$