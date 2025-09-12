# Collatz Processor with Parallel Execution
A Python script that reads pairs of integers from a file and efficiently calculates the maximum Collatz sequence length within the specified range. The program uses parallel processing to significantly speed up the calculations for large number ranges.

## The Collatz Conjecture
The Collatz Conjecture is a famous unsolved problem in mathematics. It states that for any positive integer n, the following iterative sequence will eventually reach the number 1:

* If n is even, the next number is n / 2.
* If n is odd, the next number is 3n + 1.

The "Collatz sequence length" is the number of steps it takes for a number to reach 1. For example, the sequence for the number 6 is 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1, which has a length of 9.

This program finds the number with the longest sequence length within a given range.
