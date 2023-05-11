# A simple function that calculates BMI

weight = float(input("What is your weight in kg? "))
height = float(input("What is your height in meters? "))

body_mass_index = round(weight/height ** 2)

if body_mass_index < 18.5:
    print(f"Your BMI is {body_mass_index} and you are Underweight.")
elif body_mass_index < 25:
    print(f"Your BMI is {body_mass_index} and you have a Normal weight.")
elif body_mass_index < 30:
    print(f"Your BMI is {body_mass_index} and you are Overweight.")
elif body_mass_index < 35:
    print(f"Your BMI is {body_mass_index} and you are Obese.")
else:
    print(f"Your BMI is {body_mass_index} and you are Clinically obese.")
