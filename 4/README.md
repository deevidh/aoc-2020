# AoC - Day 4

[https://adventofcode.com/2020/day/4](https://adventofcode.com/2020/day/4)

I was woken by terrifying loud #thundersnow at 4:55am, so I figured it was a sign that I should start coding ay 5am (when the challenge was released!)  I found implementing and debugging the second part pretty tedious, and I had to debug it using the test data in the challenge description.  Luckily I managed to get some sleep afterwards.

I'm not that happy with my scrappy code (so many conditionals!) so I may re-work this.

TIL:

- I'm sure it's not the most effective approach, but this was the first time I have defined a function and applied to an iterable using map, then collected the results together using numpy:
```python
def func(x): return re.match('cid:', x)
cid_map = list(map(func, fields))
if not numpy.any(cid_map):
```