number = input("Enter the number : ")
print("you have entered : ", end="")

""" eval is short for "evaluate." In this 
form, the text typed by the user is evaluated as an expression to produce the 
value that is stored into the variable. So, for example, the string 113211 becomes the number 32"""

print(number)

number2 = eval(input("Enter number : "))
print("You've entered : " ,number2) 