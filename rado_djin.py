Enter file contents hereimport random
stchislo = random.randint(1,1000)
wtchislo = random.randint(1,1000)
trchislo = random.randint(1,1000)

while izbor == 3

izbor = input("izberi: 1 - nagore, 2 - nadolo, 3 - pozna") 
if izbor == 3
print(trchislo)
print ("game over")

if izbor == 2
trchislo =random.randint(1,stchislo)
print(trchislo)

if izbor == 1
trchislo =random.randint(stchislo,1000)
print (trchislo)
