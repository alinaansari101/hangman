import random

word_list = ["iggybiggyboogy", "camel", "monkey"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)

display = []
len = len(chosen_word)


underscores = 0

while underscores < len:
  display.append("_")
  underscores += 1

tries = 6

while tries > 0:
  guess = input("Guess a letter: ").lower()
  is_match = False

  # check if character
  for i in range(len):
    if chosen_word[i] == guess:
      display[i] = chosen_word[i]
      is_match = True
      print("Correct")
      
    
  # win condition
  if "".join(display) == chosen_word:
    print("You win")
    break
    print(display)  

  # wrong try
  if is_match == False:
    tries -= 1
    print("Wrong")
  else:
    print(display)
    
  # lose condition
  if tries == 0:
      print("You lose")
      break

  print(stages[tries])
