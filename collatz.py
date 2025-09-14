import sys
from concurrent.futures import ProcessPoolExecutor

def collatz_total_count(n):
    """
    Calculates the total count of numbers in a Collatz sequence.
    This function is designed to be run in parallel.
    """
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def main(input_filename):
    """
    Main part of the program.
    Reads pairs of numbers from a file and processes them in parallel
    with extensive error handling.
    """
    try:
        # Check if the file is readable and not empty.
        with open(input_filename, 'r') as file:
            content = file.read().strip()
            if not content:
                print(f"Error: The input file '{input_filename}' is empty.", file=sys.stderr)
                return
            file.seek(0) # Reset file pointer to the beginning

            # Use a ProcessPoolExecutor for parallel execution.
            with ProcessPoolExecutor() as executor:
                for line_number, line in enumerate(file, 1):
                    # Use a list to store lines to be processed
                    line_to_process = []
                    line = line.strip()
                    if not line:
                        continue  # Skip empty lines

                    # Replace special characters with spaces
                    cleaned_line = line.replace('\n', ' ').replace('\t', ' ')

                    try:
                        # Handle multiple numbers on one line, separated by various whitespace
                        numbers_str = cleaned_line.split()

                        # Handle errors if there are not exactly two numbers per line
                        if len(numbers_str) != 2:
                            print(f"Error on line {line_number}: Expected exactly two numbers, but found '{line}'. Skipping.", file=sys.stderr)
                            continue

                        i, j = map(int, numbers_str)

                    except ValueError:
                        print(f"Error on line {line_number}: Invalid number format in '{line}'. Skipping.", file=sys.stderr)
                        continue

                    # Input validation for the numbers themselves
                    if not (i > 0 and j > 0):
                        print(f"Error on line {line_number}: Numbers must be positive integers. Skipping '{line}'.", file=sys.stderr)
                        continue

                    # The Collatz problem allows the smaller number to be second.
                    start, end = min(i, j), max(i, j)

                    print(f"Processing range from {start} to {end}...")

                    # Map the function over the range of numbers
                    results = executor.map(collatz_total_count, range(start, end + 1))
                    max_total_count = max(results)

                    print(f"Result for {i} {j}: {max_total_count}\n")

    except FileNotFoundError:
        print(f"Error: The input file '{input_filename}' was not found.", file=sys.stderr)
    except PermissionError:
        print(f"Error: Insufficient permissions to read the file '{input_filename}'.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Get the filename from command-line arguments or use a default.
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: python collatz_processor.py <input_file_path>", file=sys.stderr)
        print("Using default file 'test-input.txt' for demonstration.\n")
        main("test-input.txt")
