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
  #if input <=1
  else:
    print(numInt, " is not a prime number.")
    num = input("Enter a number: ")
print("Goodbye.")