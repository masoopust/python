
def part1():
    print("Vytáhni si plánek třetího patra.")
    print (f"Tvůj příběh začíná v UC9. Sedíš v lavici po škole, zůstal jsi tam sám a pracuješ na tvém ročníkovém projektu.\nNajednou se rozezní nefunkční rozhlas a ty uslysíš podivným hlasem.")
    print ("Vím, že tu někde jsi. Jdu si pro Tebe. Boj se.\nV hlavě si říkáš. JAK JE MOŽNÉ ŽE TEN ROZHLAS FUNGUJE? KDO TO JE? PROČ PO MNĚ JDE?\nMUSÍM IHNED UTÉCT!!! ")
    print (f"Rychle si sbalíš věci a otevřeš dveře z UC9. Kam se vydáš?\nBude to doleva k linux učebně (1), půjdeš za tvojí třídní, paní Gébovou, ji zachránit do kabinetu a budeš doufat, že se ti nic nestane (2) či se rozhodneš jít o patro níž rovnou a nebudeš nic riskovat (3)? ")
    Ch1 = int(input ("Jak jsi se rozhodl? : "))
    if Ch1 == 1:
        print (f"Utíkáš doleva kolem UC10 a slyšíš hlasy, vydáš se tam?(Ano/Ne)")
        Ch2 = input ()
        if Ch2 == "Ano":
            import UC10
            Krepelkova = UC10.nj
            Krepelkova()
        elif Ch2 == "Ne":
         print("Pokračuješ dál a doběhneš k zadnímu schodišti, kterým se vydáš do druhého patra.")
    elif Ch1 == 2:
        print("Doběhl jsi do kabinetu paní Gébové a pana Stejskala. Oba byli vevnitř, ty jsi jim popsal situaci a oba dva začali utíkat s tebou.")
        print("Společně jste seběhli do druhého patra.")
    elif Ch1 == 3:
       print("Seběhneš do druhého patra, z vrchu slyšíš křičet paní Gébovou s panem Stejskalem a ty jsi rád, že jsi té neznáme věci unikl a žiješ.")















