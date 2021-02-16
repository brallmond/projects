def red(word): return "\033[91m" + word + "\033[00m"
def green(word): return "\033[92m" + word + "\033[00m"
def yellow(word): return "\033[93m" + word + "\033[00m"
def blue(word): return "\033[94m" + word + "\033[00m"
def purple(word): return "\033[95m" + word + "\033[00m"
def cyan (word): return "\033[95m" + word + "\033[00m"

import random as rand
import numpy as np
import itertools as itt

NUM_1 = 3
NUM_2 = 5
NUM_3 = 10

WORD_1 = "FIZZ"
WORD_2 = "BUZZ"
WORD_3 = "BAZZ"

STR_1 = red(WORD_1)
STR_2 = green(WORD_2)
STR_3 = blue(WORD_3)

print("RULES: If the number given is divisible by {} say {}, if divisible by {} \
say {}, and if divisible by {} say {}. If divisible by multiple numbers, add \
both words (no spaces).".format(NUM_1, WORD_1, NUM_2, WORD_2, NUM_3, WORD_3))

def put_together(perms):
  out_array = []
  for i in range(len(perms)):
    elem = ''
    j = 0
    while j<(len(perms[0])):
      elem += perms[i][j]
      j+=1
    out_array.append(elem)
  return out_array

WORD_BANK_init = [WORD_1, WORD_2, WORD_3]
TWO_WORDS = list(itt.combinations(WORD_BANK_init,2))
THREE_WORDS = list(itt.combinations(WORD_BANK_init,3))

WORD_BANK_init.extend(put_together(TWO_WORDS))
WORD_BANK_init.extend(put_together(THREE_WORDS))

WORD_BANK = [] 
for word in WORD_BANK_init:
  WORD_BANK.append(word.upper())
  WORD_BANK.append(word.lower())
  WORD_BANK.append(word.capitalize())

def fizzbuzz(j):
  word = ""
  if (j % NUM_1 == 0):
    word += WORD_1
  if (j % NUM_2 == 0):
    word += WORD_2
  if (j % NUM_3 == 0):
    word += WORD_3
  if (word == ""):
    word = j
  return word

def fizzbuzz_color(j):
  word = ""
  if (j % NUM_1 == 0):
    word += STR_1
  if (j % NUM_2 == 0):
    word += STR_2
  if (j % NUM_3 == 0):
    word += STR_3
  if (word == ""):
    word = j
  return word

if __name__ == "__main__":
  used_numbers = []
  end = 100
  while True:
    number = rand.randint(1,end+1)
    if number in used_numbers:
      continue
    else:
      used_numbers.append(number)
      np.sort(used_numbers)

      result = fizzbuzz(number)
      result_color = fizzbuzz_color(number)

      print("The number is {}.".format(number))
      
      ans = raw_input("What do you say? ")

      if type(result) == str:
        if ans == result or ans == result.capitalize() or ans == result.lower():
          print("Nice.")
        else:
          print("Nope, it should have been {}. Drink.".format(result_color))
      else:
        if ans == str(result):
            print("Nice.")
        else:
          print("Nope, it should have been {}. Drink.".format(result_color))
