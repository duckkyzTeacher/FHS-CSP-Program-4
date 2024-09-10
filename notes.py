# Arithmetic Operations #
#**Learning objectives**
#
#After this section:
#
# * You will be able to use variables in various arithmetic operations
# * You will know how to deal with numbers in user input
# * You will know how to cast values into other fundamental data types

#   |Operator	|Purpose							|Example	|Result	|
#   |+			|Addition							|2 + 4		|6		|
#   |-			|Subtraction						|10 - 2.5	|7.5	|
#   |*			|Multiplication						|-2 * 123	|-246	|
#   |/			|Division (floating point result)	|9 / 2		|4.5	|
#   |//			|Division (integer result)			|9 // 2		|4		|
#   |%			|Modulo								|9 % 2		|1		|
#   |**			|Exponentiation						|2 ** 3		|8		|

## Live Demo ##
# Multiple Operations
#height = 172.5
#weight = 68.55
## the Body Mass Index, or BMI, is calculated by dividing body mass with the square of height
## height is converted into metres in the formula
#bmi = weight / (height / 100) ** 2
#print(f"The BMI is {bmi}")
#
# Int vs Float Division
#x = 3
#y = 2
#
#print(f"/ operator {x/y}")
#print(f"// operator {x//y}")
#
# Casting
#input_str = input("Which year were you born? ")
#year = int(input_str)
#print(f"Your age at the end of the year 2021: {2021 - year}" )
#
#year = int(input("Which year were you born? "))
#print(f"Your age at the end of the year 2021: {2021 - year}" )
#
#height = float(input("What is your height? "))
#weight = float(input("What is your weight? "))
#height = height / 100
#bmi = weight / height ** 2
#print(f"The BMI is {bmi}")

