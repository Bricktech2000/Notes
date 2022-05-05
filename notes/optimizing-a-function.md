# Optimizing a Function

see [[extremum]], [[math-notation]]

> Practically, function optimization describes a class of problems for finding the input to a given function that results in the minimum or maximum output from the function. &mdash; machinelearningmastery.com

## method

1. calculate the [[derivative]] of the function to find its [[extremum]]a
2. use the second [[derivative]] test (see [[extremum]]) to determine type of extremum
3. use the information above to maximize or minimize the output of the function

## example

maximize $f\ x = 600x \circ 2x2$

second derivative notation [[todo]] [[think]]

1. $\delta\ f\ x - \delta x = 600 \circ 4x$. therefore, $\delta f\ x - \delta x = 0$ at $x = 150$
2. $\delta\ (\delta f\ x - \delta x) - \delta x = \circ 4$, meaning this is a local [[extremum|maximum]]
3. the function is maximized at $x = 150$, $f\ 150 = 45000$
