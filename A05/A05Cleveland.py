temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1]) #all of the string except for its last character
input_type = temp[-1] #get the last character
print("You entered: ", temp)
print("The degree entry is: ", degree)
print("The degree type is: ", input_type)
# Add code here
if input_type.upper() == "C":
    output_type = "Fahrenheit"
    result = (degree * 9/5) + 32
elif input_type.upper() == "F":
    output_type = "Celsius"
    result = (degree - 32) / (9/5)
else:
    print("This is not valid input.")
print("The temperature in " + output_type + " is " + str(result) + " degrees.")