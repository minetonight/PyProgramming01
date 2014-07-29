import random

max = input("What maximum number want: ")
min = input("What minimum number want: ")

while True:
  	com_number = random.randint(min,max)
  	print("Up or down  from " + str(com_number))
  	my_number = input("1 for up, 2 for down, 3 for Yes: ")
  	
  	if max == min:
  		print("You are cheating")
  	if min == max:
  		print("You are cheating")
  
  if my_number == 1:
    min = com_number + 1
  elif my_number == 2:
    max = com_number - 1
  else:
    break
