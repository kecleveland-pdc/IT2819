# Programming Courses Game

# Mainline

def main():
    programming_courses={"Computer Concepts":"IT 1025",\
        "Programming Logic":"IT 1050",\
        "Java Programming":"IT 2670",\
        "C++ Programming":"IT 2650",\
        "Python Programming":"IT 2800"}

    print ("Learn your programming courses!\n")

    correct=0
    incorrect=0
  
    # Game Loop
    for key, value in programming_courses.items():
        response = input("What is the course number of " + key + ": ")
        if response == value:
            print("That's Correct!")
            correct += 1
        else:
            print("That's Incorrect!")
            incorrect += 1

    # Display correct and incorrect answers
    print ("You missed ",incorrect," courses.")
    print ("You got ",correct," courses.\n")

# Entry Point
response=""
while (response!="n"):
    main()
    response=input("\n\nPlay again?(y/n)\n# ")
