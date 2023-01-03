import random
from random_word import RandomWords


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


word_generator =  RandomWords()
chosen_word = word_generator.get_random_word()

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
      
      
    
  # win condition
  if "".join(display) == chosen_word:
    print("You win")
    break
    print(display)  
    print(f"The word was {chosen_word}, you guessed correctly!")

  # wrong try
  if is_match == False:
    tries -= 1
  
  else:
    print(display)
    
  # lose condition
  if tries == 0:
      print("You lose")
      print(f"The word was {chosen_word}, you guessed wrong!")
      break

  print(stages[tries])
