# Adding the digits of a number

a = input ("Write down a two digit number ")

first_digit=int(a[0])
second_digit=int(a[1])

sum_of_digits = str(first_digit + second_digit)

print(f"The sum of the digits in {a} is {sum_of_digits}")