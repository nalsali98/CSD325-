"""
Module 2 – BMI Calculator (BUGGY for debugging practice)
Author: Noor Al Salihi
Bug: uses w / h instead of w / (h*h) which makes BMI too large.
"""

def calculate_bmi(height_m: float, weight_kg: float) -> float:
    # BUG HERE: missing square on height
    return weight_kg / height_m   # <-- wrong

def classify_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def read_positive_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
            if val > 0:
                return val
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid number (e.g., 1.75).")

def main():
    h = read_positive_float("Enter height in meters (e.g., 1.75): ")
    w = read_positive_float("Enter weight in kg (e.g., 68): ")
    bmi = calculate_bmi(h, w)
    category = classify_bmi(bmi)
    print(f"BMI (BUGGY) = {bmi:.2f} → {category}")

if __name__ == "__main__":
    main()
    
