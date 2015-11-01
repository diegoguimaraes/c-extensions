# c-extensions
Sample Python C extensions based on Python Cookbook

Build the extension: `make build`

Try it:
```
$ python3
>>> import sample
>>> sample.gcd(35, 42)
7
>>> sample.in_mandel(0, 0, 500)
1
>>> sample.in_mandel(2.0, 1, 500)
0
>>> sample.divide(42, 8)
(5, 2)
>>>
```

Clear the build: `make clean`
