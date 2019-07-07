print("Assignment - written by Keaunna Cleveland")
num = input("Enter a number: ")

while num.upper()!= "X":
  # check integer
  if num.isdigit() != True:
    print("A number must be entered.")
    quit() 
  #convert str to integer
  numInt = int(num)
  #prime > 1
  if numInt > 1:
    print("Check for factors.")
    for i in range(2,numInt-1):
      if numInt % i == 0 and numInt != 2:
          print(numInt, "is not a prime number")
          print(str(i) + " times " + str(int(numInt / i)) + " is " + str(numInt))
          break
    else:
      print(numInt, "is a prime number.")
  else:
    print(numInt, "is not a prime number.")
  num = input("Enter a number: ")
print("Goodbye.")