from time import time
from multiprocessing import Pool, cpu_count


def single_factorize(number):
    """
    Find all divisors of a given number.

    Parameters:
    - number (int): The number to factorize.

    Returns:
    - list: A list of divisors for the given number.
    """
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    print(f"The divisors of {number} are: {divisors}")
    return divisors


def synchronous_factorize(*numbers):
    """
    Factorize each number from the given sequence synchronously.

    Parameters:
    - *numbers (int): List of numbers to factorize.

    Returns:
    - list: A list of lists, where each sublist contains the divisors of
            a number from the input sequence.
    """
    results = [single_factorize(number) for number in numbers]
    return results


def parallel_factorize(*numbers):
    """
    Parallel factorization of numbers using multiprocessing.

    This function utilizes all available CPU cores to factorize each number
    in parallel.

    Parameters:
    - *numbers (int): List of numbers to factorize.

    Returns:
    - list: A list of lists, where each sublist contains the divisors of
            a number from the input sequence.
    """
    with Pool(cpu_count()) as pool:
        results = pool.map(single_factorize, numbers)
    return results


if __name__ == "__main__":
    print("Synchronous factorisation...")
    # Measure synchronous execution time
    start_sync = time()
    a, b, c, d = synchronous_factorize(128, 255, 99999, 10651060)
    end_sync = time()

    print("Parallel factorisation...")
    # Measure parallel execution time
    start_parallel = time()
    a, b, c, d = parallel_factorize(128, 255, 99999, 10651060)
    end_parallel = time()

    print(f"\nSynchronous execution time: {end_sync - start_sync} seconds")
    print(f"Parallel execution time: {end_parallel - start_parallel} seconds")

    # Assertions to verify the results match expected outcomes
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158,
                 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212,
                 2662765, 5325530, 10651060]

    print("\nAll assertions passed!")
