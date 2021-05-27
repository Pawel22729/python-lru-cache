### Python LRU cache
* This project implements LRU cache logic for heavy factorial calculation
	
## Technologies
* Written with Python 3.9.4
* Requires Python 3+
	
## Execution
* Script can be executed in following way

```
python main.py
```

## Output
Script will output information about
* Factorial calculation time
* Cache hits
* Cache miss
* Cache evictions
* Cache stack with calculation a list of calculation results in FILO queue

## Sample execution
```
❯ python main.py

### Cache size init: 3

Calculate factorial for: 4
Calculation time: 0.000042

### Cache status:

Cache hits: 0
Cache miss: 1
Cache evic: 0

Cache stack

-> 24

Calculate factorial for: 5
Calculation time: 0.000023

### Cache status:

Cache hits: 0
Cache miss: 2
Cache evic: 0

Cache stack

-> 120
-> 24

Calculate factorial for: 6
Calculation time: 0.000022

### Cache status:

Cache hits: 0
Cache miss: 3
Cache evic: 0

Cache stack

-> 720
-> 120
-> 24
```

## Unittests
* Tests are performing sequential calculation on a set of predefined numbers
* Suite runs twice on the same set of numbers where first one is considered COLD (cache empty), and second HOT (cache full)
* Test can be modified to test different variants of cache size and different set of numbers

```
❯ python unittests.py
Calculating cold factorial for 4
Calculating cold factorial for 26
Calculating cold factorial for 836
Calculating cold factorial for 9172
Calculating cold factorial for 75234
Calculating cold factorial for 123456
__main__.lruTest.testColdCache: 6.580
Calculating hot factorial for 4
Calculating hot factorial for 26
Calculating hot factorial for 836
Calculating hot factorial for 9172
Calculating hot factorial for 75234
Calculating hot factorial for 123456
__main__.lruTest.testWarmCache: 0.000
----------------------------------------------------------------------
Ran 2 tests in 6.580s

```