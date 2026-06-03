def calculate_bmi(height: float, weight: float) -> float:
    """
    Calculate Body Mass Index (BMI)
    height: meters
    weight: kilograms
    """
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive values")

    bmi = weight / (height ** 2)
    return round(bmi, 2)


def calculate_bmr(height: float, weight: float, age: int, gender: str) -> float:
    """
    Calculate Basal Metabolic Rate (BMR) using Harris-Benedict equation
    height: cm
    weight: kg
    age: years
    gender: male | female
    """
    if height <= 0 or weight <= 0 or age <= 0:
        raise ValueError("Height, weight and age must be positive")

    gender = gender.lower()

    if gender == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == "female":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Gender must be 'male' or 'female'")

    return round(bmr, 2)