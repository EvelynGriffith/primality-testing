# Primality Testing

## Evelyn Griffith

## Program Output

### Use six fenced code blocks to provide output from different runs of `primality` with different inputs

`poetry run primality --number 49979687 --approach efficient`

```
😄 Attempting to determine if 49979687 is a prime number!

✨ What divisors were found? 1,49979687
✨ Was this a prime number? Yes
```

`poetry run primality --number 49979687 --approach exhaustive`

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

`poetry run primality --number 12345678 --approach exhaustive`
```
😄 Attempting to determine if 12345678 is a prime number!

✨ What divisors were found? 0,1
✨ Was this a prime number? No
```

`poetry run primality --number 103553 --approach efficient`
```
😄 Attempting to determine if 103553 is a prime number!

✨ What divisors were found? 1,103553
✨ Was this a prime number? Yes
```

`poetry run primality --number 103553 --approach exhaustive`
```
😄 Attempting to determine if 103553 is a prime number!

✨ What divisors were found? 1,103553
✨ Was this a prime number? Yes
```

#### Three outputs from running the exhaustive algorithm

TODO: Provide the specific command that you ran to produce this output
TODO: Use a fenced code block to provide the output for this command.

TODO: Provide the specific command that you ran to produce this output
TODO: Use a fenced code block to provide the output for this command.

TODO: Provide the specific command that you ran to produce this output
TODO: Use a fenced code block to provide the output for this command.

#### Three outputs from running the efficient algorithm

TODO: Provide the specific command that you ran to produce this output
TODO: Use a fenced code block to provide the output for this command.

TODO: Provide the specific command that you ran to produce this output
TODO: Use a fenced code block to provide the output for this command.

TODO: Provide the specific command that you ran to produce this output
TODO: Use a fenced code block to provide the output for this command.

## Performance Analysis

TODO: Provide one paragraph that states which algorithm is fastest, by how much
it is faster, and how you knew that the it was faster, referencing the data in
the aforementioned command outputs to support your response.

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
