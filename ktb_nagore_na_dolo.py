import random

max = input("kakvo maksimalno chislo iskash: " )
min = input("kakvo minimalno chislo iskash: " )

while True
   com_chislo = random.randint(max,min)
   print("nagore ili nadolo e moeto" str(comchislo))
   moeto_chislo = input("1 e nagore, 2 e nadolo,3 e vyarno")
   if moeto_chislo == 1:
      min = com_chislo + 1
   elif moeto_chislo == 2:
      max = max - com_chislo
   else moeto_chislo == 3:
      print ("pecelish")
      break
