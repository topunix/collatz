# CPU-parallel Collatz sequence engine for large integer ranges.
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

## Prerequisites
* Python 3.6 or higher.

## How to Run
1. __Save the script:__ Ensure the collatz_processor.py file is saved in a directory on your computer.

2. __Prepare an input file:__ Create a text file (e.g., input_data.txt) with one or more pairs of positive integers, separated by spaces or other whitespace, on each line. You can also include comments with a # at the beginning of the line.

3. __Example__ `input_data.txt`:
```python
# Calculate for two small ranges
1 10
100 200

# A very large range that benefits from parallelism
50000 60000

# Example of invalid input
1 five
```
3. __Run from the command line:__ Open your terminal or command prompt and navigate to the directory where you saved the files. Run the script by providing the input file path as a command-line argument:
```python
python collatz_processor.py input_data.txt
```
If you run the script without a file path, it will default to using a file named test-input.txt.

## How It Works
The core of the program is its ability to parallelize the Collatz calculation.

1. __File Reading:__ The script reads the input file line by line, gracefully skipping empty lines or comments.

2. __Data Parsing:__ It attempts to parse two numbers from each valid line, handling any formatting errors and providing descriptive error messages to the user without crashing.

3. __Why Not NumPy?:__ The Collatz calculation is a good example of an __"embarrassingly parallel"__ problem, but not a __vectorizable__ one.

    * __Vectorization__ (what NumPy excels at) is about applying a single operation to an entire array of numbers at once. For example, squaring every number in a list. The Collatz problem is different because each step in the sequence depends on the result of the previous step (n -> n/2 or n -> 3n + 1), so you can't calculate them all at once.

    * __Parallelism__ is about running many independent tasks at the same time. While the steps within a single Collatz sequence are sequential, the calculation for the number 50,000 is completely independent of the calculation for 50,001. This allows us to run these tasks in parallel, with each CPU core handling a different number, which is a perfect fit for this problem.

4. __Parallel Execution:__ For each valid number pair (i, j), the script creates a range of numbers from min(i, j) to max(i, j).

5. __ProcessPoolExecutor:__ The executor.map() function then takes the collatz_total_count function and applies it to every number in the range, running these tasks in parallel across all available CPU cores.

6. __Finding the Maximum:__ Once all the parallel calculations are complete, max() is used to find the highest total count from the results.

7. __Output:__ The script prints the original numbers and the final maximum Collatz total count to the console.

## Code Structure
* `collatz_total_count(n)`: A function that calculates the length of a single Collatz sequence. It is designed to be "map-able," meaning it takes a single argument and performs a CPU-intensive task, which is ideal for parallel processing.

* `main(input_filename)`: The main entry point of the script that handles file I/O, error handling, and orchestrates the parallel execution.

* `if __name__ == "__main__":`: This block ensures the main function is called only when the script is executed directly. It also handles command-line arguments.

## License
This project is licensed under the MIT License.


