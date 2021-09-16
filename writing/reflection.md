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

```
def human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    # produce a human-readable value for a bool
    # True --> "Yes"
    # False --> "No"
    if answer != True:
        return "No"
    else:
        return "Yes"
```

This code is telling the function to assign the variable "answer" to an inputed boolean and then convert it into a string value. Then the finction will move into a if statement that suggests that if the variable answer (or the number inputted) is not equal to True, meaning that it is not a prime number, than the function will return the word "No". However, if the function determines that the number is a prime number (or True) then it will file into the else statement which will return the word "Yes".

#### A function signature that defines the command-line interface for `primality`

```
@cli.command()
def primality(
    number: int = typer.Option(5),
    profile: bool = typer.Option(False),
    approach: PrimalityTestingApproach = PrimalityTestingApproach.efficient,
) -> None:
    """Use iteration to perform primality testing on a number and run a profiling data collection if requested."""
    # create a console for rich text output
    console = Console()
    # create an empty primality_tuple
    primality_tuple: Tuple[bool, List[int]]
    # use the efficient primality testing algorithm
    if approach.value == PrimalityTestingApproach.efficient:
        # Reference for more details:
        # https://github.com/joerick/pyinstrument
        # perform profiling on the execution of the primality test
        profiler.start()
        primality_tuple = primality_test_efficient(number)
        # do not perform profiling
        profiler.stop()
    # use the exhaustive primality testing algorithm
    elif approach.value == PrimalityTestingApproach.exhaustive:
        # Reference for more details:
        # https://github.com/joerick/pyinstrument
        profiler.start()
        primality_tuple = primality_test_exhaustive(number)
        # perform profiling on the execution of the primality test
        # do not perform profiling
        profiler.stop()
    # display the results of the primality test
    was_prime_found = primality_tuple[0]
    divisor_list = primality_tuple[1]
    console.print(f":smile: Attempting to determine if {number} is a prime number!")
    console.print()
    console.print(
        f":sparkles: What divisors were found? {pretty_print_list(divisor_list)}"
    )
    console.print(
        f":sparkles: Was this a prime number? {human_readable_boolean(was_prime_found)}"
    )
    # display the results of the profiling if that option was requested
    if profile:
        console.print()
        console.print(
            f":microscope: Here's profile data from performing primality testing on {number}!"
        )
        profiler.print()
``` 

TODO: Write at least one paragraph to explain the request source code

### What was the greatest challenge that you faced when completing this assignment?

TODO: Provide a one-paragraph response that answers this question in your own words.

### Based on your experiences with this project, what is one way in which you want to improve?

TODO: Provide a one-paragraph response that answers this question in your own words.
