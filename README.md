# Factorization

This repository contains a Python program designed to demonstrate the use of multiprocessing for factorizing numbers. 
It showcases both synchronous and parallel approaches to factorization, allowing for a comparative analysis of execution times under different processing strategies.

## Features

- **Single Factorization:** A function that computes all the divisors of a single number.
- **Synchronous Factorization:** Sequentially factorizes each number in a given list.
- **Parallel Factorization:** Utilizes multiprocessing to factorize each number in the list in parallel, taking advantage of multiple CPU cores.
- **Performance Comparison:** Measures and compares the execution time of both synchronous and parallel approaches.

## Installation and Usage

    # Clone the repository to the local machine:
    $ https://github.com/alex-nuclearboy/goit-python-web-hw3-factorize.git
    # Navigate to the directory containing main.py
    $ cd goit-python-web-hw3-factorize
    # Run the program
    $ python3 main.py

This will execute the factorization of predefined numbers and print the execution time for both synchronous and parallel processing to the console.