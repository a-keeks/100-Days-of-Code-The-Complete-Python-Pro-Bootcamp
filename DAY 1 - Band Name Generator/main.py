#inputs
num1 = int(input("What is the first number: "))
num2 = int(input("What is the second number: "))
product= str(num1*num2)
mystring = "The product of your two numbers is " 
print( mystring  + product)

#Counting characters in a string
name = str(input("What is your name?"))
characters=str(len(name))
mystring = "There are " + characters + " characters in your name."

print(mystring)

# Switch the values of two variable around

a = input("What is your a? ")
b = input("What is your b? ")

print("a =", b)
print("b =", a)