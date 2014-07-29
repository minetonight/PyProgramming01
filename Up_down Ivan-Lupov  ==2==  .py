import random

min = input("What is minimum number: ")
max = input("What is minimum number: ")

com_number = random.randint(min,max)

while True:
  
  my_number = input("Write number: ")
  
  if my_number == com_number:
    print("Win")
    break
  else:
    print("Game over")
