# AoC - Day 1

https://adventofcode.com/2020/day/1

After initially tackling this with nested loops, I then sought out a more elegant solution using [itertools](https://docs.python.org/3/library/itertools.html) (which looks like a pretty neat module).

TIL:
- `itertools.combinations(iterable, r)` returns tuples of length r of all the possible combinations of the input iterable.
- In python 3.8+ you can use [math.prod](https://docs.python.org/3/library/math.html#math.prod) to give the product of all elements in an iterable.