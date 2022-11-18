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

#Write your code below this line 👇
# for i in (rock, paper, scissors):
#   print(i)
# for i in range(0, 9):
choicearr = ["Rock", "Paper", "Scissors"]
hch = int(input("What's your choice? 0 for Rock/ 1 for Paper/ 2 for Scissors: "))
cch = random.randint(0, 2)
# for i in range(0, 10):
#   print(random.randint(0, 2))
diff = cch - hch
if diff == 0:
  print(f"Game Drawn.  You chose {hch}{choicearr[hch]}. Computer chose {cch}{choicearr[cch]}")
else:
  if diff in [1, -2]:
    print(f"Computer won. You chose {hch}{choicearr[hch]}. Computer chose {cch}{choicearr[cch]}")
  elif diff in [2, -1]:
    print(f"You won. You chose {hch}{choicearr[hch]}. Computer chose {cch}{choicearr[cch]}")   
  else:
    print(f"Error. You chose {hch}{choicearr[hch]}. Computer chose {cch}{choicearr[cch]}")
    