import os
import random
import time

# nevar double down uz split
# neradas J Q K A tā vietā r vnk vērtība 10
# toties strada, ka A ir 11 un 1

dileris_summa=0
tava_summa=0
split_summa=0
nauda=500
kartis=[0,1,2,3,4,5,6,7,8,9,10,10,10,10,11]
tt=""
teksts=".------.            _     _            _    _            _    \n|A_  _ |.          | |   | |          | |  (_)          | |   \n|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __\n| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /\n|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < \n`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\\n      |  \/ K|                            _/ |                \n      `------'                           |__/     \n                                                    -LK version"

for burts in teksts:
    tt+=burts
    os.system("cls")
    print(tt)
    time.sleep(.005)
time.sleep(2)

while True:
    os.system('cls')
    w=0
    ww=0
    z=0
    zz=0
    zzz=0
    d=0
    p=0
    n=0
    vel=["","","","","","","","","","","",]
    vell=["","","","","","","","","","","",]
    velll=["","","","","","","","","","","",]
    t=""
    t1="vēlvienu kārti"
    t3="sadalīt"
    tb=""
    ss=""

    a=kartis[random.randint(2,14)]
    aa=kartis[random.randint(2,14)]
    aaa=kartis[random.randint(2,14)]

    dileris_summa=a+d
    tava_summa=aa+aaa

    likme=int(input(f"Jūsu nauda ir {nauda}€\nIevadiet likmi. "))
    nauda=nauda-likme
    if nauda<0: break
    for i in range(100):
        # if ww>1: break
        www=0
        os.system('cls')

        if n>-7000:
            if tava_summa>21: 
                if aa==11 and tava_summa>21:
                    aa=1
                    tava_summa=tava_summa+aa-11
                elif aaa==11 and tava_summa>21:
                    aaa=1
                    tava_summa=tava_summa+aaa-11
                else:w=1

        else:
            if tava_summa>21:
                if aaa==11 and tava_summa>21:
                    aaa=1
                    tava_summa=tava_summa+aaa-11
                else:
                    www=www+1
                    tava_summa=0
            if split_summa>21:
                if ss==11 and split_summa>21:
                    ss=1
                    split_summa=split_summa+aaa-11
                else:
                    www=www+1 
                    split_summa=0
        
        print(f"       .=(((=.       \n      i;'   `:i               Nauda:{nauda}€\n      !__   __!      \n     (~(_)-(_)~)              Dīleris:({dileris_summa})   {a} {d} {vell[0]} {vell[1]} {vell[2]} {vell[3]}\n      !   n   !               Tu:({tava_summa})        {aa} {aaa} {vel[0]} {vel[1]} {vel[2]} {vel[3]} {vel[4]} {vel[5]} {vel[6]}\n       \  -  /                {t}      {ss} {velll[0]} {velll[1]} {velll[2]} {velll[3]} {velll[4]} {velll[5]}\n       !`---'!       \n      /`-._.-'\               Likme:{likme}\n _.-~'\_/ |o\_/`~-._ \n'         |o        `\n")
        print(f"       1           {tb}   2      {tb}     3       {tb}        4")
        print(f"{t1}     palikt     {t3}     dubultot lejup")

        if w!=0: break
        if www>1: break
        if ww!=0: break
        if p==0:    
            izvele=int(input("\nIzvēlietes, ko vēlaties darīt. "))

            if izvele==1:
                n=n+1
                vel[z]=kartis[random.randint(2,14)]
                tava_summa=tava_summa+vel[z]
                for i in range(z+1):
                    if vel[z-i]==11 and tava_summa>21:
                        vel[z]=1
                        tava_summa=tava_summa+vel[z-i]-11
                z=z+1
                
        if izvele==2:
            if d==0:
                d=kartis[random.randint(2,14)]
                # print(d)
                dileris_summa=dileris_summa+int(d)
                    
            if dileris_summa<17:
                vell[zz]=kartis[random.randint(2,14)]
                # print(vell[zz])
                dileris_summa=dileris_summa+int(vell[zz])

                for i in range(z+1):
                    if vell[zz-i]==11 and dileris_summa>21:
                        vell[zz]=1
                        dileris_summa=dileris_summa+vell[zz-i]-11
                if d==11 and dileris_summa>21:
                    d=1
                    dileris_summa=dileris_summa+d-11
                if a==11 and dileris_summa>21:
                    a=1
                    dileris_summa=dileris_summa+a-11

                zz=zz+1
                if dileris_summa<17:p=1

            if dileris_summa>21:
                if n>-7000:
                    w=2
                if n<-7000:
                    ww=10
                    if tava_summa<dileris_summa and split_summa<dileris_summa:ww=11
            if dileris_summa>16 and dileris_summa<22:
                if n>-7000:
                    if tava_summa>dileris_summa:w=2
                    elif tava_summa==dileris_summa:w=3
                    elif tava_summa<dileris_summa:w=1
                if n<-7000:
                    if tava_summa>dileris_summa and split_summa>dileris_summa:ww=30
                    if tava_summa<dileris_summa and split_summa<dileris_summa:ww=40
                    if tava_summa<dileris_summa and split_summa>dileris_summa:ww=50
                    if tava_summa>dileris_summa and split_summa<dileris_summa:ww=50
                    if tava_summa==dileris_summa and split_summa>dileris_summa:ww=60
                    if tava_summa>dileris_summa and split_summa==dileris_summa:ww=60
                    if tava_summa==dileris_summa and split_summa>dileris_summa:ww=70
                    if tava_summa>dileris_summa and split_summa==dileris_summa:ww=70
                    
        if izvele==3:
            if n<-1:
                velll[zzz]=kartis[random.randint(2,14)]
                split_summa=split_summa+velll[zzz]
                for i in range(z+1):
                    if velll[zzz-i]==11 and split_summa>21:
                        velll[zzz]=1
                        split_summa=split_summa+vel[zzz-i]-11
                t=f"Split:({split_summa})"
                zzz=zzz+1
            if n==0 and aa==aaa:
                if nauda-likme>=0:
                    nauda=nauda-likme
                    likme=likme*2
                    t=f"Split:({split_summa})"
                    split_summa=aa
                    tava_summa=tava_summa-aa
                    ss=aa
                    aa=""
                    t1="vēlvienu kārti (Tu)"
                    t3="vēlvienu kārti (Split)"
                    tb="      "
                    n=-80085

        if izvele==4:
            if n==0:
                if nauda-likme>=0:
                    nauda=nauda-likme
                    likme=likme*2
                    
                    vel[z]=kartis[random.randint(2,14)]
                    tava_summa=tava_summa+vel[z]
                    for i in range(z+1):
                        if vel[z-i]==11 and tava_summa>21:
                            vel[z]=1
                            tava_summa=tava_summa+vel[z-i]-11
                    izvele=2
                    p=1

    if w==2:
        laimests=likme*2
        print(f"\nDīleris aizgāja pāri. Laimests={laimests}€ ")
        nauda=nauda+laimests
    if w==1:print("\nJūs zaudējāt. ")
    if w==3:
        print("\nNeizšķirts. ")
        nauda=nauda+likme

    if www==2:print("\nJūs zaudējāt abos. ")
    if ww==10:
        laimests=likme*2
        print(f"\nDīleris aizgāja pāri. Abas rokas uzvar. Laimests={laimests}€ ")
        nauda=nauda+laimests
    if ww==11:
        laimests=likme
        print(f"\nDīleris aizgāja pāri. Viena roka uzvar. Laimests={laimests}€ ")
        nauda=nauda+laimests
    if ww==30:
        laimests=likme*2
        print(f"\nAbas rokas uzvar. Laimests={laimests}€ ")
        nauda=nauda+laimests
    if ww==40:print("Abas rokas zaud. ")
    if ww==50:
        laimests=likme
        print(f"\nViena roka uzvar uzvar. Laimests={laimests}€ ")
        nauda=nauda+laimests
    if ww==60:
        laimests=likme*1.5
        print(f"\nViena roka uzvar uzvar. Otra neizšķirts. Laimests={laimests}€ ")
        nauda=nauda+laimests
    if ww==70:
        laimests=likme*0.5
        print(f"\nViena roka uzvar zaudē. Otra neizšķirts. Laimests={laimests}€ ")
        nauda=nauda+laimests

    spelet=input("Spiediet enter, lai spēlētu atkal. ")
