# calculating BMI

# 1st input: enter height in meters 
height = float(input("What is your height in metres? " ))
# 2nd input: enter weight in kilograms
weight = int(input("What is your weight in kilograms? " ))

BMI = round(weight/height**2, 2)

print(f"Your BMI is {BMI} to 2 decimal places.")

