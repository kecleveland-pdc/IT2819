temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1]) #all of the string except for its last character
input_type = temp[-1] #get the last character
print("You entered: ", temp)
print("The degree entry is: ", degree)
print("The degree type is: ", input_type)
# Add code here
if input_type.upper() == "C":
    print("Celsius")
elif input_type.upper() == "F":
    print("Fahrenheit")
else:
    print("This is not valid input.")
# print("The temperature in", output_type, "is", result, "degrees.