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

🔬 Here's profile data from performing primality testing on 103553!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 21:20:55  Samples:  1
 /_//_/// /_\ / //_// / //_'/ //     Duration: 0.016     CPU time: 0.016
/   _/                      v4.0.3

Program: primality --number 103553 --approach exhaustive --profile

0.010 primality  primality\main.py:106
└─ 0.010 primality_test_exhaustive  primality\main.py:55
```

`poetry run primality --number 12345678 --approach exhaustive`
```
😄 Attempting to determine if 12345678 is a prime number!

✨ What divisors were found? 0,1
✨ Was this a prime number? No

🔬 Here's profile data from performing primality testing on 12345678!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 21:22:58  Samples:  0
 /_//_/// /_\ / //_// / //_'/ //     Duration: 0.000     CPU time: 0.000
/   _/                      v4.0.3

Program: primality --number 12345678 --approach exhaustive --profile

No samples were recorded.
```

`poetry run primality --number 49979687 --approach exhaustive`

```
😄 Attempting to determine if 49979687 is a prime number!

✨ What divisors were found? 1,49979687
✨ Was this a prime number? Yes

🔬 Here's profile data from performing primality testing on 49979687!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 21:24:42  Samples:  1
 /_//_/// /_\ / //_// / //_'/ //     Duration: 4.714     CPU time: 4.719
/   _/                      v4.0.3

Program: primality --number 49979687 --approach exhaustive --profile

4.711 primality  primality\main.py:106
└─ 4.711 primality_test_exhaustive  primality\main.py:55
```

#### Three outputs from running the efficient algorithm

`poetry run primality --number 49979687 --approach efficient --profile`

```
😄 Attempting to determine if 49979687 is a prime number!

✨ What divisors were found? 1,49979687
✨ Was this a prime number? Yes

🔬 Here's profile data from performing primality testing on 49979687!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 21:25:58  Samples:  1
 /_//_/// /_\ / //_// / //_'/ //     Duration: 2.314     CPU time: 2.312
/   _/                      v4.0.3

Program: primality --number 49979687 --approach efficient --profile

2.305 primality  primality\main.py:106
└─ 2.305 primality_test_efficient  primality\main.py:81
```

`poetry run primality --number 12345678 --approach efficient --profile`

```
😄 Attempting to determine if 12345678 is a prime number!

✨ What divisors were found? 2
✨ Was this a prime number? No

🔬 Here's profile data from performing primality testing on 12345678!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 21:29:46  Samples:  0
 /_//_/// /_\ / //_// / //_'/ //     Duration: 0.000     CPU time: 0.000
/   _/                      v4.0.3

Program: primality --number 12345678 --approach efficient --profile

No samples were recorded.
```

`poetry run primality --number 103553 --approach efficient --profile`
```
😄 Attempting to determine if 103553 is a prime number!

✨ What divisors were found? 1,103553
✨ Was this a prime number? Yes

🔬 Here's profile data from performing primality testing on 103553!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 21:23:44  Samples:  1
 /_//_/// /_\ / //_// / //_'/ //     Duration: 0.007     CPU time: 0.000
/   _/                      v4.0.3

Program: primality --number 103553 --approach efficient --profile

0.005 primality  primality\main.py:106
└─ 0.005 primality_test_efficient  primality\main.py:81
```

## Performance Analysis

The efficiency algorithm is faster by 49% in the example for number 49979687. The other two numbers were so fast to calculate for the computer that both outputs ended up being 0.000. I dont know what this means, but according to my code it seems that the amount of time that the code cuts off gets bigger the larger the input is. Because I added a few digits with the first number, the difference in timing was larger becasue there were more things to calculate through, but when I went down to numbers that were smaller like the second and third example it seems that the change in time that it saves decreases.

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

This is essentially the function that calls upon all the other functions in the file. It first takes the variable "number" and defines it as an integer, then it defines the variable "profile" as a boolean, and finally it defines "approach" as None but only through the efficient function. The it uses an if statement to approach a value which the user inputs and tells the computer to approach the value through the efficient function. Then it will start the profiler and call upon the primality_tuple variable which it originally defined as a boolean and a list of integers. Then it will, finally, officially call upon the primality_test_efficient function and ask for the variable "number" which as you may recall it already defined as an integer. Once the primality_test_efficient function completes it's job the profiler will stop, and the function will determine if it needs the futher elif statment from line 27 of the above code.
If the function determines that the user is trying to approach the number not from an efficient perspective but from an exahustive approach, it will use everything below the elif statement. It will start the profiler then, using the primality_tuple variable it will call upon the primality_test_exhaustive function looking for the variable "number" and once that function has done its job the bigger function will tell the profiler to stop.
Then the function will move into determining what needs to be printed based on the data it found. If the function determines that the number was prime it will print the yes statement from the bool function if not it will print no. It will also print the number and its smallest divisor if it was not prime.

### What was the greatest challenge that you faced when completing this assignment?

The greatest challenge I faced when trying to run this code was that I couldn't figure out why the pyinstrument wouldn't install on my computer. I was getting a lot of weird errors that made me panick and think that I actually did mess something up when we were in SOS week, but Coby came over and helped me figure out that the actual issue was that I already had the package installed and the computer didnt want me to install it again.

### Based on your experiences with this project, what is one way in which you want to improve?

I think I said this in a previous lab, but I still get hungup in how to start things and how to be confident enough to try things even if it doesnt seem like they will work. I just need to get better at using the todos to figure out what is being asked of me.
