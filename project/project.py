import random as rd

randNum = rd.randint(1, 6)

while True:
    userChoice = input("Enter Your Number (1-6) or Quit (q) :  ")
    if(userChoice == "q" or userChoice == "Q"):
        break
    if (not userChoice.isdigit() or not (1 <= int(userChoice) <= 6)):
        print("You have to enter a number between 1 and 6.")
        continue
        
    if(userChoice == randNum):
        print("=====>>>> YOU HAVE WON THE GAME.CORRECT NUMBER IS A", randNum)
        break
    else:
        print("=====>>>> YOU HAVE LOSS THE GAME .CORRECT NUMBER IS A", randNum)
        break
