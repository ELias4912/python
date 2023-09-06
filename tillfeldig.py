import random

tilfeldig_tall = random.randint(1,100)

print(tilfeldig_tall)

svar = input("gjett et tall mellom 1-100 -> ")

if svar == tilfeldig_tall:
    print("riktig")
else: 
    print("feil")

