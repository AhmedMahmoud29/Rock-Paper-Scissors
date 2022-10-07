Zero = 0
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import py_compile
import random

print('Welcome to "Rock Paper Scissors"\n\n')
print("Type the number of of your choice:-\n")
Choice_of_The_Player = int(input("1-ROCK     2-PAPER     3-SCISSORS\n"))
Choice_of_The_Computer = random.randint(1, 3)
Options = [Zero, Rock, Paper, Scissors]

if Choice_of_The_Player >= 4 or Choice_of_The_Player < 1:
  print("Invalid input!\nGame Over!")
  
else:
  
  print("You Chose:-\n" + Options[Choice_of_The_Player])
  print("The Computer Chose:-\n" + Options[Choice_of_The_Computer])

  if Choice_of_The_Player == 1 and Choice_of_The_Computer == 3:
    print("You won!\nThe computer lost!\nGame over!")
  elif Choice_of_The_Computer == 3 and Choice_of_The_Computer == 1:
    print("You lost!\nThe computer won!\nGame over!")
  elif Choice_of_The_Player == Choice_of_The_Computer:
    print("It's a draw!\nGame over!")
  elif Choice_of_The_Player > Choice_of_The_Computer:
    print("You won!\nThe computer lost!\nGame over!")
  elif Choice_of_The_Player < Choice_of_The_Computer:
    print("You lost!\nThe computer won!\nGame over!")

import os
src = "F:\Python Projects\Rock Paper Scissors.py"
dst = "F:\Python Projects\Rock Paper Scissors(Link).py"
os.link(src, dst)