# Primality Testing

## Evelyn Griffith

## Program Output

### Use six fenced code blocks to provide output from different runs of `primality` with different inputs

#### Three outputs from running the exhaustive algorithm

`poetry run primality --number 103553 --approach exhaustive`
```
😄 Attempting to determine if 103553 is a prime number!

✨ What divisors were found? 1,103553
✨ Was this a prime number? Yes
```

`poetry run primality --number 12345678 --approach exhaustive`
```
😄 Attempting to determine if 12345678 is a prime number!

✨ What divisors were found? 0,1
✨ Was this a prime number? No
```

`poetry run primality --number 49979687 --approach exhaustive`

```
😄 Attempting to determine if 49979687 is a prime number!

✨ What divisors were found? 1,49979687
✨ Was this a prime number? Yes
```

#### Three outputs from running the efficient algorithm

`poetry run primality --number 49979687 --approach efficient`

```
😄 Attempting to determine if 49979687 is a prime number!

✨ What divisors were found? 1,49979687
✨ Was this a prime number? Yes
```

`poetry run primality --number 12345678 --approach efficient`

```
😄 Attempting to determine if 12345678 is a prime number!

✨ What divisors were found? 2
✨ Was this a prime number? No
```

`poetry run primality --number 103553 --approach efficient`
```
😄 Attempting to determine if 103553 is a prime number!

✨ What divisors were found? 1,103553
✨ Was this a prime number? Yes
```

## Performance Analysis

The efficiency algorithm is faster by 41% in the example for number 49979687. It is faster by 6% in the second example, and 9% in the third example. I dont know what this means, but according to my code it seems that the amount of time that the code cuts off gets bigger the larger the input is. Because I added a few digits with the first number, the difference in timing was larger becasue there were more things to calculate through, but when I went down to numbers that were smaller like the second and third example it seems that the change in time that it saves decreases.

## Source Code

### Describe in detail how the completed source code works

#### A function that converts a `bool` into a human readable `str` value

TODO: Use a fenced code block to provide the requested source code
TODO: Write at least one paragraph to explain the request source code

#### A function signature that defines the command-line interface for `primality`

TODO: Use a fenced code block to provide the requested source code
TODO: Write at least one paragraph to explain the request source code

### What was the greatest challenge that you faced when completing this assignment?

TODO: Provide a one-paragraph response that answers this question in your own words.

### Based on your experiences with this project, what is one way in which you want to improve?

TODO: Provide a one-paragraph response that answers this question in your own words.
