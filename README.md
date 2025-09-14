# Collatz Processor with Parallel Execution
A Python script that reads pairs of integers from a file and efficiently calculates the maximum Collatz sequence length within the specified range. The program uses parallel processing to significantly speed up the calculations for large number ranges.

## The Collatz Conjecture
The Collatz Conjecture is a famous unsolved problem in mathematics. It states that for any positive integer n, the following iterative sequence will eventually reach the number 1:

* If n is even, the next number is n / 2.
* If n is odd, the next number is 3n + 1.

The "Collatz sequence length" is the number of steps it takes for a number to reach 1. For example, the sequence for the number 6 is 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1, which has a length of 9.

This program finds the number with the longest sequence length within a given range.

### Example Input & Output:

For an input file with the line: 1 10, the program will calculate the sequence length for every number between 1 and 10. The output will be: 1 10 20, as the number 9 has the longest sequence (9 -> 28 -> 14 -> 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1), with a length of 20.

## Features
* __Parallel Processing:__ Utilizes Python's ProcessPoolExecutor to distribute the computation of Collatz sequences across multiple CPU cores, dramatically reducing processing time.

* __Robust Error Handling:__ The script is designed to handle common file and data errors, including:

   * File not found or unreadable due to permissions.

   * Empty input files.

   * Lines with incorrect number formats or non-numeric characters.

   * Lines with more or less than two numbers.

   * Non-positive integer inputs.

* __Flexible Input:__ The program can read numbers separated by various whitespace characters (spaces, tabs, newlines) on a single line.

* __Clear Output:__ Provides real-time feedback on the processing status and outputs the final result for each number pair.
