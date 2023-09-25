import random
hp = 100
pinne=0
stein=0
tau=0
naan=0

asking = True
while asking == True:
    if valg == "A" or valg == "B":
        asking = True
    else: 
#tau = random.randint(1,3)
   

def Start_rom():
    
    print ("Du er ute på havet med båten din, du ser at det bobler i vannet")

    valg = input("Hva gjør du? A: kjører nærmere B: kjører vekk -> ")
    
    if valg == "A":  
        print("Du valgte å kjøre nærmere, du stakk hånden din ned i vannet, ikke så lurt.. du blir drat under å aldri sett igjen")
  
    if valg == "B":
        print("Du kjører vekk, du får aldri vite hva det var, men du lever i hvertfall.")
        rom_2()


def rom_2():
    print("du har kjørt deg vill, gjennom den tykke tåken kan du se en øy")
    print("Hva gjør du? A: kjører mot øya B: lete etter fastland -> ")

    valg = input(" A eller B? ")

    if valg == "A":
        print("Du har nåd øya, men denne plassen gir deg en dårlig følelse.")
        øya() 


    if valg == "B":
        print("du får en dårlig følelse av den øya, du kjører vidre uten å tenke deg om.")
        borte()

def øya(): 
    global pinne, stein
    print("Hær ser du noe spesielt")
    print("Du hører en lyd mage følelsen din sier at du ikke burde sjekke, men nysjerigheten din drar deg mot den")
    valg = input("A: går å utforsker lyden B: utforsk øya for ressursser ->  ")

    if valg == "A":
        print("nysjerigheten din får det beste av deg og du drar for å sjekke lyden ut det ente opp med at du ble spist av kannibaler")

    if valg == "B":
        print("Det kan umulig være noe godt som kommer av å sjekke ut lyden ikkesant? Du begynner og samle pinner og steiner")
        pinne+=random.randint(1,3)
        stein+=random.randint(1,3)
        print(f"Du fant  {pinne} pinner og {stein} steiner")
    


def borte():
    global naan 
    print("du har kjørt deg vill,du inser du ikke kommer til å finne fastland") 
    print("du kjører tilbake til øya")
    øya()
    
    print("du har brukt hele dagen på og samle pinner du tenker at nå er den beste tide å utforske skogen")
    print("du begynner å utforske skogen du får følelsen av at noen ser på deg, men du ser ingen. du finner en leir med noen få hytter")

    valg = input("Hva gjør du? A: utforsker leiren B: uforsk hyttene -> ")

    if valg == "A":
        print("du utforsker leiren å ender opp med å finne litt naan")
        naan+=random.randint(1,3) 
        (f"Dun fant {naan} naan")
        print("Du tar brødet og løper bort så fort som du kan")
        tempel()
                                   

    if valg == "B":
        print("Du går in i en hytte, der ligger det en kannibal,") 
        print("Du snur deg rundt får og gå ut av hytten, men kannibalen våkner")
        random_encounter()

def tempel():
    print("Du finner et tempel dypt inne i skogen")



def random_encounter(): 
    global hp, pinne, stein 
    print("fight")
    Kannibal_hp = 50 
    fighting = True
    while fighting:
        print(f"\nDu har {hp} hp.")
        print(f"Kannibalen har {Kannibal_hp} hp.")
        dodge_chance = 0 
        valg = input("\nA: Slå B: Dodge -> ")
        if valg == "A":
            dmg = random.randint(1,10)
            Kannibal_hp -= dmg
            print(f"Du slo bossen for {dmg} dmg.")

        elif valg == "B":
            dodge_chance = random.randint(1,10) 
        if Kannibal_hp < 0:
            print("Kannibal er død")
            victory()

        else: # boss attack
            if dodge_chance < 2:
                Kannibal_dmg = random.randint(5,10)
                hp -=Kannibal_dmg
                print(f"Kannibal slo deg for {Kannibal_dmg} dmg.")
        if hp <1:
            print("Du er død")
            game_over()

    def game_over():
        pass

    def victory():
        pass            








Start_rom()
