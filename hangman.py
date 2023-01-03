import random
from random_word import RandomWords


STAGES = ['''
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

NUM_OF_TRIES = 6

word_generator =  RandomWords()
chosen_word = word_generator.get_random_word()

display = []
word_len = len(chosen_word)
underscores = 0

while underscores < word_len:
  display.append("_")
  underscores += 1


while NUM_OF_TRIES > 0:
  guess = input("Guess a letter: ").lower()
  is_match = False

  # check if character
  for i in range(word_len):
    if chosen_word[i] == guess:
      display[i] = chosen_word[i]
      is_match = True
      
  # win condition
  if "".join(display) == chosen_word:
    print("You win")
    print(display)
    print(f"The word was {chosen_word}, you guessed correctly!")
    

  # wrong try
  if is_match == False:
    NUM_OF_TRIES -= 1
  
  else:
    print(display)
    
  # lose condition
  if NUM_OF_TRIES == 0:
      print("You lose")
      print(f"The word was {chosen_word}, you guessed wrong!")
      break

  print(STAGES[NUM_OF_TRIES])
