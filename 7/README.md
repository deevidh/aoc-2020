# AoC - Day 7

[https://adventofcode.com/2020/day/7](https://adventofcode.com/2020/day/7)

Had a busy day and didn't really approach this in a thoughtful manner, so my code is pretty scrappy.  Got there in the end though once I wrapped my head around the recursion.

**TIL:**

- It's possible to put a conditional into a list comprehension, but you have to change the order a little.  For example, you can write:

    ```python
    for item in list:
        if conditional:
            expression
    ```
    as
    ```python
    [ expression for item in list if conditional ]
    ```