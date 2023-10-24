def patro2():
    print("Vytáhni si plánek druhého patra.")
    print(f"Dostal jsi se do druhé patra, co tě tu může asi čekat jiného než POSLUCHÁRNA?")
    print(f"Blížíš se k posluchárně a samozřejmě, že tam někdo je. Je tam pan Ženčiča s elektronikou (1) nebo Pan Losert se zaečkem(2) ?")
    A1= int(input("Co myslíš? : "))
    if A1 == 1:
        print("Máš pravdu!! Je tam pan Ženčica a aby tě pustil pryč, musíš mu vypočítat kvadratickou rovnici.")
        print("Zadánní tvé kvadratické rovnice je a = 5, b = 57, c = 6")
        print("Ty máš ale naštěstí u sebe kvadratickou kalkulačku z dřívějška tak ji použiješ, POZOR ať tě pan Ženčica nevidí.")
        from math import sqrt, pow

        a = int(input("Zadej kořen a : "))
        b = int(input("Zadej kořen b : "))
        c = int(input("Zadej kořen c : "))

        D = (pow(b,2) - 4 *a*c)
        print (f"{D}") 
        if D > 0:

            x1 = (-b + sqrt(D))/ (2 *a)
            print(f"Kořen x1 je {x1}")
            x2 = (-b - sqrt(D))/ (2 *a)
            print(f"Kořen x2 je {x2}")
        else :
            print("Diskriminant je záporný, rovnice nemá řešení.")
        print("Máš štěstí! Pan Ženčica tě neviděl, je spokojený a můžeš pokračovat zase o patro níže.")    
    if A1 == 2:
        print("Máš pravdu!! Je tam pan Losert, BÝT TEBOU TAK SI RADĚJI NACHYSTÁM PISÁTKO, KALKULAČKU A PAPÍR,\n aby tě pustil pryč, musíš mu vypočítat jeden ze šesti příkladů, který si náhodně vybereš pomocí jeho oblíbené kostky.")
        starter = int(input("Až budeš psychicky připraven hodit napiš číslo 13, oblíbené číslo pana Loserta.\n"))
        from random import randint
        priklad = randint (1,6)
        print (f"Vylosoval jsi si příklad číslo {priklad}")


        if priklad == 1 :
            vysl = 7000
            print("Uslyšíš známou větu: Všechno ze stolu, pisátko, kalkulačka a máš na to pět minut, můžeš začít.")
            print("Tvé zadání zní:\n Stanovte odpor vodiče, kterým prochází proud 25mA při napětí 175V. Výsledek zadej v ohmech.")
            Yvysl = int(input("Kolik ohmů : " ))
            if vysl == Yvysl:
                print(f"Výborně, můžeš domů!")
            else:
                print(f"Raději mi zmiz z očí! Správný výsledek je {vysl}.")


        if priklad == 2 :
            vysl = 30
            print("Uslyšíš známou větu: Všechno ze stolu, pisátko, kalkulačka a máš na to pět minut, můžeš začít.")
            print("Tvé zadání zní:\n Určete napětí na spotřebiči, jehož odpor je 1,5kΩ a kterým prochází proud 20mA. Výsledek zadej ve voltech.")
            Yvysl = int(input("Kolik voltů : " ))
            if vysl == Yvysl:
                print(f"Výborně, můžeš domů!")
            else:
                print(f"Raději mi zmiz z očí! Správný výsledek je {vysl}.")


        if priklad == 3 :
            vysl = 800
            print("Uslyšíš známou větu: Všechno ze stolu, pisátko, kalkulačka a máš na to pět minut, můžeš začít.")
            print("Tvé zadání zní:\n Stanovte výkon, vykonaný elektrickým proudem za 2 hodiny. Proud 10A prochází vodičem o odporu 8 ohmů. Výsledek zadej ve wattech.")
            Yvysl = int(input("Kolik wattů : " ))
            if vysl == Yvysl:
                print(f"Výborně, můžeš domů!")
            else:
                print(f"Raději mi zmiz z očí! Správný výsledek je {vysl}.")


        if priklad == 4 :
            vysl = 40
            print("Uslyšíš známou větu: Všechno ze stolu, pisátko, kalkulačka a máš na to pět minut, můžeš začít.")
            print("Tvé zadání zní:\n Vypočítejte, kolik hodin může svítit žárovka o příkonu 25W, než spotřebuje energii 1 kWh. Výsledek zadej v hodinách.")
            Yvysl = int(input("Kolik hodin : " ))
            if vysl == Yvysl:
                print(f"Výborně, můžeš domů!")
            else:
                print(f"Raději mi zmiz z očí! Správný výsledek je {vysl}.")

        
        if priklad == 5 :
            vysl = 20
            print("Uslyšíš známou větu: Všechno ze stolu, pisátko, kalkulačka a máš na to pět minut, můžeš začít.")
            print("Tvé zadání zní:\n Elektrická kamna jsou připojena na napětí 220V a mají příkon 4,4kW. Určete proud, který odebírají. Výsledek zadej v ampérách.")
            Yvysl = int(input("Kolik ampér : " ))
            if vysl == Yvysl:
                print(f"Výborně, můžeš domů!")
            else:
                print(f"Raději mi zmiz z očí! Správný výsledek je {vysl}.")
        
        if priklad == 6:
            print("Dnes máš štěstí, protože jsi hodil šestku a na šestku pan Losert nezkouší a pustil tě dále.")




        




    
































