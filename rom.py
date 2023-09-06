hp = 100
 
def rom_1():
    print("Du er nå i rom 1, her skjer det et eller annet")
    valg = input("Velg A for rom 2, velg B for rom 3")
    if valg == "A":
        rom_2() # starter rom 2
    if valg == "B":
        rom_3() # start rom 3
 
def rom_2():
    global hp
    print("Her var det en stor brann, du tok skade")
    hp -= 30
    print("Du har nå", hp, "liv igjen..")
 
    if hp <= 0:
        game_over()
 
    rom_1()
 
def rom_3():
    print("Du er i rom nr 3, vil du tilbake til rom nr 1?")
 
def game_over():
    print("Du er død.")
    exit()
 
rom_1() 