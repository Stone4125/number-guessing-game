import random 
choix_computer = random.randint(1,100)

print ("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
print ("You have 10 attempts remaining to guess the number.")
choix_user = int(input("Make a guess: "))
if level == "easy":
  for i in range(10):
    if choix_user == choix_computer:  
      print (f"You got it! The answer was {choix_computer}.")
    elif choix_user > choix_computer:  
      print ("too high.\n")
      print (f"You have {9-i} attempts remaining to guess the number.")
      hoix_user = int(input("Make a guess: \n"))
     
    elif choix_user < choix_computer:  
      print ("too low.\n")
      print (f"You have {9-i} attempts remaining to guess the number.")
      choix_user = int(input("Make a guess: \n"))

    elif i == 9:
      print (f"You've run out of guesses, you lose. The answer was {choix_computer}.")
  


elif level == "hard":
  for i in range(5):
    if choix_user == choix_computer:  
      print (f"You got it! The answer was {choix_computer}.")
    elif choix_user > choix_computer:  
      print ("too high.\n")
      print (f"You have {4-i} attempts remaining to guess the number.")
      hoix_user = int(input("Make a guess: \n"))
    elif choix_user < choix_computer:  
      print ("too high.\n")
      print (f"You have {4-i} attempts remaining to guess the number.")
      hoix_user = int(input("Make a guess: \n"))
    if i == 4:
      print (f"You've run out of guesses, you lose. The answer was {choix_computer}.")
      break