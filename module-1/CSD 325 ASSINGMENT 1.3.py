"""
Assignment 1.3 – On the Wall + Flowchart
Author: Noor Al Salihi
Description:
  Asks the user how many bottles of beer are on the wall,
  passes that number to a function that counts down to 1,
  prints grammatically correct lyrics, and then reminds the
  user to buy more beer at the end.
"""

def bottles_countdown(n: int) -> None:
    """Print the bottles-of-beer countdown from n to 1.
    Uses 'bottle(s)' grammar and shows the next count.
    """
    # Defensive: if n < 1, do nothing
    if n is None or n < 1:
        return

    for i in range(n, 0, -1):
        # Current label (singular/plural)
        curr_label = "bottle" if i == 1 else "bottles"
        next_i = i - 1  # next number
        # Display the song line
        line = (f"{i} {curr_label} of beer on the wall, {i} {curr_label} of beer. "
                f"Take one down and pass it around, {next_i} bottle(s) of beer on the wall.")
        print(line)

def read_positive_int(prompt: str = "Enter number of bottles: ") -> int:
    """Read a positive integer (>=1) from the user, re-prompting on bad input."""
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if val >= 1:
                return val
            else:
                print("Please enter a whole number 1 or greater.")
        except ValueError:
            print("Please enter a valid whole number (for example, 3).")

def main():
    n = read_positive_int("Enter number of bottles: ")
    bottles_countdown(n)
    print("Time to buy more beer!")

if __name__ == "__main__":
    main()
