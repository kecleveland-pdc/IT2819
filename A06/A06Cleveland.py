is_running = True
while (is_running):
    temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")
    degree = int(temp[:-1]) #all of the string except for its last character
    input_type = temp[-1] #get the last character
    print("You entered: ", temp)
    print("The degree entry is: ", degree)
    print("The degree type is: ", input_type)

    if input_type.upper() == "C":
        output_type = "Fahrenheit"
        result = (degree * 9/5) + 32
    elif input_type.upper() == "F":
        output_type = "Celsius"
        result = (degree - 32) / (9/5)
    elif input_type.upper() == "X":
        print("Goodbye!")
        exit()
    else:
        print("Input proper convention.")
        continue
    is_running = False
print("The temperature in " + output_type + " is " + str(result) + " degrees.")