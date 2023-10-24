def prvni_patro():
    vys1 = "receipt-invoice-customer"
    vys3 = "school-goose-shark"


    print("Vytáhni si plánek prvního patra.")
    print("Fuuha ten příklad mi dal zabrat, pomyslíš si. Chceš jít k hlavnímu vchodu, ale schodiště je zablokované, musíš tedy kolem kabinetu jazykářů.")
    print("Nejobávanější TRIO na škole, paní Matlerová, paní Heglasová a pan Deutsch, doufáš, že tě už nic nepotká a můžeš co nejrychleji utéct.")
    print("Přece jen ti jde o život a máš v patách neznámou identitu, která opravila rozhlas a jde si pro tebe.")
    print("Dojdeš ke kabinetu a nakonec se rozhodneš je varovat také. Zaťukáš a čekáš, kdo ti otevře, protože po většinu času je tam pani Matlerová.")
    from random import randint
    tvujucitel = randint(1,3)
    #print(f"Slyšíš kroky a prudce ti otevře {tvujucitel}. Co to pro tebe znamená? ")


    if tvujucitel == 1:
        print("Paní Heglasová na tebe vytáhne její Business English a musíš ji přeložit tato slovíčka: ")
        print("Podle následující předlohy přelož:  účtenka-faktura-zákazník ")
        A1 = input("účtenka-faktura-zákazník ")
        if A1 == vys1:
            print("Potřebovala jsem si jen ověřit zda-li jste to vy, teď vás mohu ukrýt do bezpečí a počkat na mého manžela, který nám pomůže utéct.")
            print("Počkali jste společně na manžela, který vás oba dva protáhl oknem a vy jste přežili.")
            print("TOTO JE ÚSPĚŠNÝ KONEC HRY, GRATULUJI K ÚTĚKU")
        else:
            print("Bohužel toto není správna odpověď a nemohu vás připustit do našeho kabinetu.")
            print("Zabouchla za vámi a mezitím jste ztratil moc času. Duch pana Lorence vás dostihl a zavlékl do měření a co se s vámi stalo nechcete vědět.")
            print("TOTO JE NEÚSPĚŠNÝ KONEC HRY, PROHRAL JSI, MŮŽEŠ SE POKUSIT ZNOVU.")


    if tvujucitel == 2:
        print("Paní Matlerová na tebe vytáhne její filozofii a chce po tobě slyšet smysl života : ")
        print("Řekni mi alespoň 50 slov o smyslu života : ")
        A2 = input("Smysl života : \n ")
        print("Paní Matlerové je jedno co jsi řekl, ona je spokojená a vezme tě do bezpečí jejich kabinetu, kde spolu počkáte na příjezd Policie, která vás bezpečně eskortuje ven ze školy.")
        print("TOTO JE ÚSPĚŠNÝ KONEC HRY, GRATULUJI K ÚTĚKU")

    
    if tvujucitel == 3:
        print("Pan Deutsch na tebe vytáhne jeho anglickou konverzaci a chce po tobě přeložit tato slovíčka : ")
        print("Podle následující předlohy přelož:  škola-husa-žralok ")
        A3 = input("škola-husa-žralok : ")
        if A3 == vys3:
            print("Potřeboval jsem si jen ověřit zda-li jste to vy, teď vás mohu ukrýt do bezpečí mého kabinetu.")
            print("Šli jste spolu do jeho kabinetu a po cestě vás doběhl duch pana Lorence,který vás zavlékl do měření a co se s vámi stalo nechcete vědět. ")
            print("TOTO JE NEÚSPĚŠNÝ KONEC HRY, PROHRAL JSI, MŮŽEŠ SE POKUSIT ZNOVU.")
        else:
            print("Bohužel toto není správna odpověď a nemohu vás připustit do našeho kabinetu.")
            print("Zabouchl za vámi a mezitím jste ztratil moc času. Duch pana Lorence vás dostihl a zavlékl do měření a co se s vámi stalo nechcete vědět.")
            print("TOTO JE NEÚSPĚŠNÝ KONEC HRY, PROHRAL JSI, MŮŽEŠ SE POKUSIT ZNOVU.")















