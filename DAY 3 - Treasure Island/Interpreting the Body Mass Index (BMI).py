# Interpreting the Body Mass Index (BMI) 
# calculating BMI

# 1st input: enter height in meters 
height = float(input("What is your height in metres? "))
# 2nd input: enter weight in kilograms
weight = int(input("What is your weight in kilograms? "))

BMI = round(weight/height**2, 2)

if BMI < 18.5: #Under 18.5 they are underweight
    print(f"Your BMI is {BMI}, and you are underweight.")

elif BMI >= 18.5 and BMI < 25: #Over 18.5 but below 25 they have a normal weight
    print(f"Your BMI is {BMI}, and you have a normal weight.")

elif BMI >= 25 and BMI < 30: #Equal to or over 25 but below 30 they are slightly overweight
    print(f"Your BMI is {BMI}, and you are slightly overweight.")

elif BMI >= 30 and BMI < 35: #Equal to or over 30 but below 35 they are obese
    print(f"Your BMI is {BMI}, and you are obese.")

elif BMI >= 35: #Equal to or over 35 they are clinically obese
    print(f"Your BMI is {BMI}, and you are clinically obese.")
