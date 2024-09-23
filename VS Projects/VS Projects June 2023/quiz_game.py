print("Welcome to my quiz game!!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print ("Okay, let's play!!")
score = 0

answer = input("How old is Sherry? ")
if answer.lower() == "25":
    print("Correct!!")
    score +=1
else :
    print("Incorrect!")

answer = input("What is my favourite colour? ")
if answer.lower() == "blue":
    print("Correct!!")
    score +=1
else :
    print("Incorrect!")

answer = input("What is my younger bro's name? ")
if answer.lower() == "brandon":
    print("Correct!!")
    score +=1
else :
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 3) * 100) + " %")
