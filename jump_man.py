import keyboard
import time
import os
import random

s=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
p=["#"," "]

tt=""
teksts="\n       _                         __  __             _ \n      | |                       |  \/  |           | |\n      | |_   _ _ __ ___  _ __   | \  / | __ _ _ __ | |\n  _   | | | | | '_ ` _ \| '_ \  | |\/| |/ _` | '_ \| |\n | |__| | |_| | | | | | | |_) | | |  | | (_| | | | |_|\n  \____/ \__,_|_| |_| |_| .__/  |_|  |_|\__,_|_| |_(_)\n                        | |                           \n                        |_|                           \n                                          -LK version  "

for burts in teksts:
    tt+=burts
    os.system("cls")
    print(tt)
    time.sleep(.005)
time.sleep(2)

print("\n             3-lēni    2-vidēji     1-ātri")
dif=int(input("                Izvēlieties grūtību! "))
atrums=25*dif

punkti=0
an=9
a=0
bn=0
b=0
z=0
while True:
    punkti+=1
    if atrums>15:
        if punkti%10==0:
            atrums=int(atrums-1)

    z=z-1
    if s[0]=="@" and p[0]=="#":
        break
    

    if a!=8:
        a=random.randint(1,8)
        an=16
    if a==8:
        if an>=0:
            s[an]=" " 
            an=an-1
            s[an]="@"
        if an<0:
            s[0]=" "
            a=0

    if b!=8:
        b=random.randint(1,8)
        bn=16
    if b==8:
        if bn>=0:
            s[bn]=" " 
            bn=bn-1
            s[bn]="@"
        if bn<0:
            s[0]=" "
            b=0

    for i in range(atrums):
        time.sleep(0.005)
        if z<0:
            if keyboard.is_pressed(" "):
                p[1]="#"
                p[0]=""
                z=2

    os.system("cls")
    if z>0:
        print(f"\n\n{p[1]}                             punkti:{punkti}")
        print(f"\n{p[0]}{s[0]}{s[1]}{s[2]}{s[3]}{s[4]}{s[5]}{s[6]}{s[7]}{s[8]}{s[9]}{s[10]}{s[11]}{s[12]}{s[13]}{s[14]}{s[15]}{s[16]}\n-----------------------")
    if z<=0:
        p[1]=" "
        p[0]="#"
        print(f"\n\n{p[1]}                             punkti:{punkti}")
        print(f"\n{p[0]}{s[0]}{s[1]}{s[2]}{s[3]}{s[4]}{s[5]}{s[6]}{s[7]}{s[8]}{s[9]}{s[10]}{s[11]}{s[12]}{s[13]}{s[14]}{s[15]}{s[16]}\n-----------------------")  

print(f"Zaudēji! ")