import random

def play_game():
    lucky_number = random.randint(1,50)

    while True:
        user_number = int(input("Enter Your Lucky Number:"))
        if user_number == lucky_number:
          print("You Won! Game is Over")
          break
        elif user_number< lucky_number:
          print("Your Number is Too Low")
        else:
           print("Too High") 
    print("Thank You For Playing Game")        

play_game()      