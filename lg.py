import random
Joueurs = int(input("Choisissez le nombre de joueur : "))
Liste = 0
ListePseudo = []
ChoosenNBR = 0
AssassinPseudo = []
SilicaPseudo = []
KleinPseudo = []
PaysanPseudo = []
ArgoPseudo = []
KuradeelPseudo = []
AgilPseudo = []
KibaouPseudo = []
if Joueurs == 8 :
    Assassin = 3
    Silica = 1
    Klein = 1
    Paysan = 2
    Argo = 1
elif Joueurs == 9:
    Assassin = 3
    Silica = 1
    Klein = 1
    Paysan = 3
    Argo = 1
elif Joueurs == 10:
    Assassin = 4
    Silica = 1
    Klein = 1
    Paysan = 3
    Argo = 1
elif Joueurs == 11:
    Assassin = 3
    Silica = 1
    Klein = 1
    Paysan = 4
    Argo = 1
    Kuradeel = 1
elif Joueurs == 12:
    Assassin = 4
    Silica = 1
    Klein = 1
    Paysan = 3
    Argo = 1
    Kuradeel = 1
    Agil = 1
elif Joueurs == 13:
    Assassin = 4
    Silica = 1
    Klein = 1
    Paysan = 4
    Argo = 1
    Kuradeel = 1
    Agil = 1
elif Joueurs == 14:
    Assassin = 5
    Silica = 1
    Klein = 1
    Paysan = 4
    Argo = 1
    Kuradeel = 1
    Agil = 1
elif Joueurs == 15:
    Assassin = 4
    Silica = 1
    Klein = 1
    Paysan = 5
    Argo = 1
    Kuradeel = 1
    Agil = 1
    Kibaou = 1

while Liste < Joueurs :
    Pseudo = input("Rentrez les pseudos des joueurs de la partie : ")
    ListePseudo.append(Pseudo)
    Liste += 1
Liste2 = (Liste-1)
if Joueurs == 8:
    while Assassin != 0:
        ChoosenNBR = random.randint(0, Liste2)
        AssassinPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Assassin -= 1
        Liste2 -= 1
    while Silica != 0:
        ChoosenNBR = random.randint(0, Liste2)
        SilicaPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Silica -=1
        Liste2 -= 1
    while Klein != 0:
        ChoosenNBR = random.randint(0, Liste2)    
        KleinPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Klein -= 1
        Liste2 -= 1
    while Argo != 0:
        ChoosenNBR = random.randint(0, Liste2)
        ArgoPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Argo -= 1
        Liste2 -= 1
    while Paysan != 0:
        while Liste2 != 0:
            ChoosenNBR = random.randint(1, Liste2)
            PaysanPseudo.append(ListePseudo[ChoosenNBR])
            ListePseudo.pop(ChoosenNBR)
            Paysan -= 1
            Liste2 -= 1    
        PaysanPseudo.append(ListePseudo[0])
        ListePseudo.pop(0)
        Paysan -= 1
elif Joueurs == 9:
    while Assassin != 0:
        ChoosenNBR = random.randint(0, Liste2)
        AssassinPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Assassin -= 1
        Liste2 -= 1
    while Silica != 0:
        ChoosenNBR = random.randint(0, Liste2)
        SilicaPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Silica -=1
        Liste2 -= 1
    while Klein != 0:
        ChoosenNBR = random.randint(0, Liste2)    
        KleinPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Klein -= 1
        Liste2 -= 1
    while Argo != 0:
        ChoosenNBR = random.randint(0, Liste2)
        ArgoPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Argo -= 1
        Liste2 -= 1
    while Paysan != 0:
        while Liste2 != 0:
            ChoosenNBR = random.randint(1, Liste2)
            PaysanPseudo.append(ListePseudo[ChoosenNBR])
            ListePseudo.pop(ChoosenNBR)
            Paysan -= 1
            Liste2 -= 1    
        PaysanPseudo.append(ListePseudo[0])
        ListePseudo.pop(0)
        Paysan -= 1
elif Joueurs == 10:
    while Assassin != 0:
        ChoosenNBR = random.randint(0, Liste2)
        AssassinPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Assassin -= 1
        Liste2 -= 1
    while Silica != 0:
        ChoosenNBR = random.randint(0, Liste2)
        SilicaPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Silica -=1
        Liste2 -= 1
    while Klein != 0:
        ChoosenNBR = random.randint(0, Liste2)    
        KleinPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Klein -= 1
        Liste2 -= 1
    while Argo != 0:
        ChoosenNBR = random.randint(0, Liste2)
        ArgoPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Argo -= 1
        Liste2 -= 1
    while Paysan != 0:
        while Liste2 != 0:
            ChoosenNBR = random.randint(1, Liste2)
            PaysanPseudo.append(ListePseudo[ChoosenNBR])
            ListePseudo.pop(ChoosenNBR)
            Paysan -= 1
            Liste2 -= 1    
        PaysanPseudo.append(ListePseudo[0])
        ListePseudo.pop(0)
        Paysan -= 1
elif Joueurs == 11:
    while Assassin != 0:
        ChoosenNBR = random.randint(0, Liste2)
        AssassinPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Assassin -= 1
        Liste2 -= 1
    while Silica != 0:
        ChoosenNBR = random.randint(0, Liste2)
        SilicaPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Silica -=1
        Liste2 -= 1
    while Klein != 0:
        ChoosenNBR = random.randint(0, Liste2)    
        KleinPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Klein -= 1
        Liste2 -= 1
    while Argo != 0:
        ChoosenNBR = random.randint(0, Liste2)
        ArgoPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Argo -= 1
        Liste2 -= 1
    while Kuradeel != 0:
        ChoosenNBR = random.randint(0, Liste2)
        KuradeelPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Kuradeel -= 1
        Liste2 -= 1
    while Paysan != 0:
        while Liste2 != 0:
            ChoosenNBR = random.randint(1, Liste2)
            PaysanPseudo.append(ListePseudo[ChoosenNBR])
            ListePseudo.pop(ChoosenNBR)
            Paysan -= 1
            Liste2 -= 1    
        PaysanPseudo.append(ListePseudo[0])
        ListePseudo.pop(0)
        Paysan -= 1
elif Joueurs == 12:
    while Assassin != 0:
        ChoosenNBR = random.randint(0, Liste2)
        AssassinPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Assassin -= 1
        Liste2 -= 1
    while Silica != 0:
        ChoosenNBR = random.randint(0, Liste2)
        SilicaPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Silica -=1
        Liste2 -= 1
    while Klein != 0:
        ChoosenNBR = random.randint(0, Liste2)    
        KleinPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Klein -= 1
        Liste2 -= 1
    while Argo != 0:
        ChoosenNBR = random.randint(0, Liste2)
        ArgoPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Argo -= 1
        Liste2 -= 1
    while Kuradeel != 0:
        ChoosenNBR = random.randint(0, Liste2)
        KuradeelPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Kuradeel -= 1
        Liste2 -= 1
    while Agil != 0:
        ChoosenNBR = random.randint(0, Liste2)
        AgilPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Agil -= 1
        Liste2 -= 1
    while Paysan != 0:
        while Liste2 != 0:
            ChoosenNBR = random.randint(1, Liste2)
            PaysanPseudo.append(ListePseudo[ChoosenNBR])
            ListePseudo.pop(ChoosenNBR)
            Paysan -= 1
            Liste2 -= 1    
        PaysanPseudo.append(ListePseudo[0])
        ListePseudo.pop(0)
        Paysan -= 1
elif Joueurs == 13:
    while Assassin != 0:
        ChoosenNBR = random.randint(0, Liste2)
        AssassinPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Assassin -= 1
        Liste2 -= 1
    while Silica != 0:
        ChoosenNBR = random.randint(0, Liste2)
        SilicaPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Silica -=1
        Liste2 -= 1
    while Klein != 0:
        ChoosenNBR = random.randint(0, Liste2)    
        KleinPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Klein -= 1
        Liste2 -= 1
    while Argo != 0:
        ChoosenNBR = random.randint(0, Liste2)
        ArgoPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Argo -= 1
        Liste2 -= 1
    while Kuradeel != 0:
        ChoosenNBR = random.randint(0, Liste2)
        KuradeelPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Kuradeel -= 1
        Liste2 -= 1
    while Agil != 0:
        ChoosenNBR = random.randint(0, Liste2)
        AgilPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Agil -= 1
        Liste2 -= 1
    while Paysan != 0:
        while Liste2 != 0:
            ChoosenNBR = random.randint(1, Liste2)
            PaysanPseudo.append(ListePseudo[ChoosenNBR])
            ListePseudo.pop(ChoosenNBR)
            Paysan -= 1
            Liste2 -= 1    
        PaysanPseudo.append(ListePseudo[0])
        ListePseudo.pop(0)
        Paysan -= 1
elif Joueurs == 14:
    while Assassin != 0:
        ChoosenNBR = random.randint(0, Liste2)
        AssassinPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Assassin -= 1
        Liste2 -= 1
    while Silica != 0:
        ChoosenNBR = random.randint(0, Liste2)
        SilicaPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Silica -=1
        Liste2 -= 1
    while Klein != 0:
        ChoosenNBR = random.randint(0, Liste2)    
        KleinPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Klein -= 1
        Liste2 -= 1
    while Argo != 0:
        ChoosenNBR = random.randint(0, Liste2)
        ArgoPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Argo -= 1
        Liste2 -= 1
    while Kuradeel != 0:
        ChoosenNBR = random.randint(0, Liste2)
        KuradeelPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Kuradeel -= 1
        Liste2 -= 1
    while Agil != 0:
        ChoosenNBR = random.randint(0, Liste2)
        AgilPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Agil -= 1
        Liste2 -= 1
    while Paysan != 0:
        while Liste2 != 0:
            ChoosenNBR = random.randint(1, Liste2)
            PaysanPseudo.append(ListePseudo[ChoosenNBR])
            ListePseudo.pop(ChoosenNBR)
            Paysan -= 1
            Liste2 -= 1    
        PaysanPseudo.append(ListePseudo[0])
        ListePseudo.pop(0)
        Paysan -= 1
elif Joueurs == 15:
    while Assassin != 0:
        ChoosenNBR = random.randint(0, Liste2)
        AssassinPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Assassin -= 1
        Liste2 -= 1
    while Silica != 0:
        ChoosenNBR = random.randint(0, Liste2)
        SilicaPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Silica -=1
        Liste2 -= 1
    while Klein != 0:
        ChoosenNBR = random.randint(0, Liste2)    
        KleinPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Klein -= 1
        Liste2 -= 1
    while Argo != 0:
        ChoosenNBR = random.randint(0, Liste2)
        ArgoPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Argo -= 1
        Liste2 -= 1
    while Kuradeel != 0:
        ChoosenNBR = random.randint(0, Liste2)
        KuradeelPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Kuradeel -= 1
        Liste2 -= 1
    while Agil != 0:
        ChoosenNBR = random.randint(0, Liste2)
        AgilPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Agil -= 1
        Liste2 -= 1
    while Kibaou != 0:
        ChoosenNBR = random.randint(0, Liste2)
        KibaouPseudo.append(ListePseudo[ChoosenNBR])
        ListePseudo.pop(ChoosenNBR)
        Kibaou -= 1
        Liste2 -= 1
    while Paysan != 0:
        while Liste2 != 0:
            ChoosenNBR = random.randint(1, Liste2)
            PaysanPseudo.append(ListePseudo[ChoosenNBR])
            ListePseudo.pop(ChoosenNBR)
            Paysan -= 1
            Liste2 -= 1    
        PaysanPseudo.append(ListePseudo[0])
        ListePseudo.pop(0)
        Paysan -= 1         
print('Les Assassins sont : %s' % AssassinPseudo)
print('Silica est : %s' % SilicaPseudo)
print('Klein est : %s' % KleinPseudo)
print('Argo est : %s' % ArgoPseudo)
print('Les Paysans sont : %s' % PaysanPseudo)
print('Kuradeel est : %s' % KuradeelPseudo)
print('Agil est : %s' % AgilPseudo)
print('Kibaou est : %s' % KibaouPseudo)
print('Les Joueurs restant sont  : %s' % ListePseudo)