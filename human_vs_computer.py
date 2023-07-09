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

# Write your code below this line 👇
print('Type "0" for rock, "1" for paper, and "2" for scissors')
option = [rock, paper, scissors]
l = ["rock", "paper", "scissors"]

try:
    human = int(input("Human pick form the number above\n"))
    print(f"Human pick {l[human]}")
    print(option[human])
    computer = random.randint(0, 2)
    print(f"Computer pick {l[computer]}")
    print(option[computer])
except:
    print("Out of range")
else:
    if human == computer:
        print("Draw")
    elif human == 0 and computer == 2:
        print("You wins")
    elif human == 1 and computer == 0:
        print("You wins")
    elif human == 2 and computer == 1:
        print("You wins")
    else:
        print("You lose")
