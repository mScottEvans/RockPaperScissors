import random 



choices = ["rock","paper","scissors"]
user_choice = input("Enter your choice(rock/paper/scissors)")
computer_choice = random.choice(choices)

print("Computer choices:", computer_choice)

if user_choice == computer_choice:
  print("It's a TIE!")
elif user_choice == "rock":
  if computer_choice == "scissors":
    print("You WON!!")
  else:
    print("Computer wins *SAD FACE*")
elif user_choice == "paper":
  if computer_choice == "rock":
    print("You WON!!")
  else:
    print("Computer wins *SAD FACE")
elif user_choice == "scissors":
  if computer_choice == "paper":
    print("You WON!!")
  else:
    print("Computer wins *SAD FACE*")

else: 
  print("Invalid choice! Try Again!")
