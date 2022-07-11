# Problem 46:
#     Goldbach's Other Conjecture
#
# Description:
#     It was proposed by Christian Goldbach that every odd composite number
#       can be written as the sum of a prime and twice a square.
#          9 =  7 + 2 × 1^2
#         15 =  7 + 2 × 2^2
#         21 =  3 + 2 × 3^2
#         25 =  7 + 2 × 3^2
#         27 = 19 + 2 × 2^2
#         33 = 31 + 2 × 1^2
#     It turns out that the conjecture was false.
#
#     What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from math import floor, sqrt
from typing import Set


def is_prime(x: int, primes: Set[int]) -> bool:
    """
    Returns True iff `x` is a prime number.

    Args:
        x      (int):      Natural number greater than 2
        primes (Set[int]): Set of all odd primes less than x

    Returns:
         (bool): True iff `x` is a prime number

    Raises:
        AssertError: if incorrect args are given
    """
    for p in primes:
        if x % p == 0:
            return False
    return True


def main() -> int:
    """
    Returns the smallest odd composite number that cannot be written as
      the sum of a prime and twice a square.

    Returns:
        (int): Smallest odd composite number not equalling the sum of a prime and twice a square
    """
    # Accumulate the set of primes discovered while searching odd numbers.
    # Technically don't need to store 2, as only odd primes are needed here.
    primes = set()

    # Check all odd numbers,
    #   storing primes as we find them,
    #   and trying to satisfy the conjecture for composites.
    x = 3
    while True:
        if is_prime(x, primes):
            primes.add(x)
        else:
            # Loop through potential values of squared number
            found = False  # Indicates if a sum was found
            y_hi = floor(sqrt((x - 3) // 2))  # Highest possible candidate for squared number of sum
            for y in range(1, y_hi+1):
                # Check whether remaining part of sum is a prime number
                if (x - 2 * y ** 2) in primes:
                    found = True
                    break
                else:
                    continue
            if not found:
                return x
        x += 2


if __name__ == '__main__':
    goldbach_breaker = main()
    print('Smallest odd composite breaking Goldbach\'s "other" conjecture:')
    print('  {}'.format(goldbach_breaker))
