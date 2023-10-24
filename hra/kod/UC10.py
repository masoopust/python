def nj():
    A1 = "Der"
    A2 = "Ich wohne in Olomouc."
    A3 = "Božena Němcová"
    A4 = "PH"
    znamka = 5
    print("Vejdeš dovnitř a tam uvidíš paní Křepelkovou zkoušet a ihned tě vyvolá k tabuli.")
    print("Protože jsi narušil moji hodinu, budeš zkoušený u tabule. V hlavě si řekneš. Ale NEEE, já nic neumím, já mám celou dobu Johna a nedávám pozor.")
    print("Paní Křepelková říká: Položím ti první otázku: Jaký člen má pes, Hund (Der/Die/Das)")
    YA1 = input()
    if YA1 == A1:
        print ("Správně")
        znamka = znamka -1
    else:
        print("CHYBA pokračujeme dále, správná odpověď je Der.") 
         
    print("Druhá otázka zní: Jak bys přeložil, Já bydlím v Olomouci.")
    YA2 = input()
    if A2 == YA2:
        print ("Působivé")
        znamka = znamka -1
    else :
        print(f"Špatně, jak jinak, správná odpověď je {A2}.")
    
    print("Protože učím i čj, začnu se ptát i na otázky z českého jazyka. Kdo napsal Babičku, poporsím celé jméno.")
    YA3 = input()
    if YA3 == A3:
        print ("Ohromující")
        znamka = znamka -1
    else:
        print(f"Vy nedáváte pozor ani v českém jazyce??? Toto jsou základy! Správná odpověď je {A3}.")
    
    print("Která písmena jsou velká v sousloví PRAŽŠKÝ HRAD?")
    YA4 = input()
    if YA4 == A4:
        print (f"správně")
        znamka = znamka -1
    else:
        print (f"Já už opravdu nevím co s vámi, je to {A4}.")

    print(f"V dálce uslyšíš podivné výkřiky a zvuky, tak se rozhodnete utéct z UC10 pryč.")


    print(f"Paní Křepelková na vás volá: DOSTAL JSTE ZA {znamka}, NEBOJTE SE, VŠE SI PÍŠU.")
    print("Mezitím jsi utekl a zadním schodištěm seběhl do druhého patra.")


