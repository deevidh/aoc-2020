# AoC - Day 4

[https://adventofcode.com/2020/day/4](https://adventofcode.com/2020/day/4)

I was woken by terrifying loud #thundersnow at 4:55am, so I figured it was a sign that I should just start coding (so for the first time I had the excitement of seeing the challenge released at 5am!)  I found implementing and debugging the second part of the challenge pretty tedious, and I had to debug it using the test data in the challenge description.  Luckily I managed to get some more sleep afterwards.

Later, I wasn't happy with my scrappy code so I rewrote the solution in `4-improved.py`.  In this approach I immediately parse the documents into dictionaries, which were then quite nice to work with.  I also optimised my code: in my initial attempt I generally validated every field first and then collected to evaluate the overall document validity.  In the improved approach I only validate what I have to, and this made it about 50% faster.  It's also much nicer to read!

**TIL:**

- In my initial attempt I defined a function and applied it to an iterable using map, then collected the results together using numpy:

    ```python 
    def func(x): return re.match('cid:', x)
    cid_map = list(map(func, fields))
    if not numpy.any(cid_map):
    ```

    I haven't used `map` or `numpy` like this before, so that was neat.  However I removed this in my improved version, as once the data was represented in a dict it was much easier to just check for the existence of the optional key.
