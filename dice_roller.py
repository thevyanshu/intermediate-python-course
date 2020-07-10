def main():
  import random
  
  dice_rolls = 2
  dice_sum = 0
  
  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    print(f'You rolled a {roll}')
    dice_sum += roll
  
if __name__== "__main__":
  main()
