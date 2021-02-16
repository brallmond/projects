"""
Give a two word phrase and number
and the left and right sides will
take turns appearing on the terminal
"""
from time import sleep
from termcolor import colored

def blink(word, duration):
  mid = word.index(' ')
  left_element = word[0:mid]
  right_element = word[mid:len(word)]
  left_color = colored(left_element, 'red')
  right_color = colored(' '*len(left_element)+right_element, 'green')
  size = 0
  while (size < int(duration)):
    print(left_color)
    sleep(0.3)
    print('\x1b[A'+'\x1b[2K'+'\x1b[A')
    print(right_color)
    sleep(0.3)
    print('\x1b[A'+'\x1b[2K'+'\x1b[A')
    size += 1

if __name__ == "__main__":
  from argparse import ArgumentParser
  parser = ArgumentParser()
  parser.add_argument('--side', '-s', dest="phrase", required=False, \
action='store', default="left right", help='Which side starts on?')
  parser.add_argument('--time', '-t', dest="duration", required=False,
default=10, action='store', help='How many blinks ya want?')
  args = parser.parse_args()
  blink(args.phrase, args.duration)
