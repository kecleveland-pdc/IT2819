print("Program Written by Keaunna Cleveland")

while True:

    temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C) : ")

    if temp[-1].upper() == "X":
        break;
    else:


        degree = int(temp[:-1]) #all of the string except for its last character

                
        input_type = temp[-1] #get the last character

        print("You entered: ", degree, input_type.upper())
        
        if input_type.upper() == "C":

                result = int(round((9 * degree) / 5 + 32))
                output_type = "Fahrenheit"
                print("The temperature in", output_type, "is", result, "degrees.")


        elif input_type.upper() == "F":

                result = int(round((degree - 32) * 5 / 9))
                output_type = "Celsius"
                print("The temperature in", output_type, "is", result, "degrees.")

        else:
          print("Input proper convention.")

print("Goodbye!")
