"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

def fib_seq(position):
    if position <= 1:
        return position
    return fib_seq(position-1) + fib_seq(position - 2)

assert fib_seq(0) == 0
assert fib_seq(1) == 1
assert fib_seq(6) == 8