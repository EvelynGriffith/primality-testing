"""Perform primality testing with both exhaustive and efficient approaches."""

from pyinstrument import Profiler  # type: ignore

from typing import Iterable, Sized
from typing import List
from typing import Tuple

from enum import Enum

import typer

from rich.console import Console

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a Profiler object to support timing program code segments
profiler = Profiler()


class PrimalityTestingApproach(str, Enum):
    """Define the name for the approach for performing primality testing."""

    exhaustive = "exhaustive"
    efficient = "efficient"


def human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    # produce a human-readable value for a bool
    # True --> "Yes"
    # False --> "No"
    if answer is not False:
        return "Yes"
    else:
        return "No"


def pretty_print_list(values: Iterable[int]) -> str:
    """Pretty print a list without brackets and adding commas."""
    # create and return a version of the list without brackets
    ls = ""
    for x in range(Sized(values)):
        if x == Sized(values) - 1:
            ls += f"{values[x]}"
        else:
            ls += f"{values[x]},"
        # and with commas in between all of the values
    return ls


def primality_test_exhaustive(x: int) -> Tuple[bool, List[int]]:
    """Perform an exhaustive primality test on the provided integer."""
    # declare the smallest_divisor with default of None
    sm_div = None
    # exhaustively search through all of the values, starting at 2
    # --> if the number is evenly divisible, then it is not prime
    for guess in range(2, x):
        if x % guess == 0:
            sm_div = guess
            return (False, [0, 1])
            break
    if sm_div is not None:
        return (False, [sm_div])
    else:
        return (True, [1, x])
    # if smallest_divisor is no longer None then the function has
    # found a non-prime number with a specific smallest_divisor
    # if the smallest_divisor is still None then the function has
    # found a prime number and it should return both itself and 1
    # make sure that the function returns:
    # --> a bool for whether or not the number was prime
    # --> a List[int] for the list with the smallest divisor for the number
    # --> if the number is prime, return the List[int] with both the number and 1


def primality_test_efficient(x: int) -> Tuple[bool, List[int]]:
    """Perform an efficient primality test on the provided integer."""
    smallest_divisor = None
    # determine first if the number is even and then confirm
    # that it does have a smallest_divisor of 2
    if x % 2 == 0:
        smallest_divisor = 2
    else:
        # use a range function that skips over the even values
        for guess in range(3, x, 2):
            if x % guess == 0:
                smallest_divisor = guess
                break
    # if the number is not even, then iteratively perform primality test
    if smallest_divisor is not None:
        # make sure that the function returns:
        # --> a bool for whether or not the number was prime
        # --> a List[int] for the list with the smallest divisor for the number
        # --> if the number is prime, return the List[int] with both the number and 1
        return (False, [smallest_divisor])
    else:
        return (True, [1, x])


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
