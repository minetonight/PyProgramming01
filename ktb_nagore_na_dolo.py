import random

min = 1
max = 1000

while True :

   com_chislo = random.randint(min, max)
   print ("nagore ili nadolo e moeto chislo" + str(com_chislo))
   moeto_chislo = input("1 e nagore, 2 e nadolo,3 e vyarno ")
    
   if moeto_chislo == 1:
		min = com_chislo + 1
   elif moeto_chislo == 2:
		max = com_chislo -1
   elif moeto_chislo == 3:
      print ("pecelish")
      break
