# AoC - Day 8

[https://adventofcode.com/2020/day/8](https://adventofcode.com/2020/day/8)

For a while I was frustrated chasing a bug in the "code fuzzer" caused by my age old enemy: updating referenced list elements rather than the copy. I thought I was on top of this, but I didn't account for the fact that my list contained lists.

**TIL:**

- When you copy a list (eg using `list()` or `copy()`), any elements in the list which are also lists still contain references to those original elements.  So in this case you need to use `copy.deepcopy()` (or in my case I just recreated the elements).