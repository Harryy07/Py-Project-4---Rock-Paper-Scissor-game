import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if 0 <= user_selection <= 2:
    print(f"User Choice : \n {game_images[user_selection]}")

comp_selection = random.randint(0,2)
print(f"Computer choice : \n {game_images[comp_selection]}")

if 0 > user_selection >= 3:
    print("You entered an invalid number, You lose")
elif user_selection == 0 and comp_selection == 1:
    print("You lose!")
elif user_selection == 0 and comp_selection == 2:
    print("You win!")
elif user_selection == 2 and comp_selection == 0:
    print("You lose")
elif user_selection == comp_selection :
    print("Its a Draw")
elif comp_selection > user_selection:
    print("you lose")
elif user_selection > comp_selection:
    print("you win")


