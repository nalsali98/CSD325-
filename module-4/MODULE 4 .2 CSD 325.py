"""
sitka_high_low_nas.py
Author: Noor Al Salihi (NAS)
Purpose: View Sitka, Alaska 2018 daily highs/lows with a simple menu.
"""

import csv
import sys
from datetime import datetime
import matplotlib.pyplot as plt

FILENAME = "sitka_weather_2018_simple.csv"


def load_weather_data(filename):
    """Load dates, highs, and lows from the CSV file."""
    dates, highs, lows = [], [], []
    try:
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                try:
                    current_date = datetime.strptime(row[2], "%Y-%m-%d")
                    high = int(row[5])
                    low = int(row[6])
                except ValueError:
                    # skip bad rows
                    continue
                else:
                    dates.append(current_date)
                    highs.append(high)
                    lows.append(low)
    except FileNotFoundError:
        print(f"Error: CSV file '{filename}' not found in the current directory.")
        sys.exit(1)
    return dates, highs, lows


def plot_data(dates, temps, title, color):
    """Plot high or low temperatures."""
    plt.figure(figsize=(10, 6))
    plt.plot(dates, temps, color=color)
    plt.title(title, fontsize=14)
    plt.xlabel("Date", fontsize=10)
    plt.ylabel("Temperature (F)", fontsize=10)
    plt.tight_layout()
    plt.show()


def main():
    """Main menu for Sitka Weather Viewer."""
    dates, highs, lows = load_weather_data(FILENAME)

    while True:
        print("\n=== Sitka Weather Viewer (2018) ===")
        print("Choose one option:")
        print("  highs  → Show daily high temperatures")
        print("  lows   → Show daily low temperatures")
        print("  exit   → Quit program")

        choice = input("Enter choice: ").strip().lower()

        if choice == "highs":
            plot_data(dates, highs, "Daily High Temperatures - 2018 (Sitka, AK)", "red")
        elif choice == "lows":
            plot_data(dates, lows, "Daily Low Temperatures - 2018 (Sitka, AK)", "blue")
        elif choice == "exit":
            print("\nExiting program. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option. Please type 'highs', 'lows', or 'exit'.")


if __name__ == "__main__":
    main()
