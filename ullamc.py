>>> def add(x, y):
...     return x + y
...
>>> wrapped = wrapper(add, 1, y=2)
>>> wrapped(3)
6
