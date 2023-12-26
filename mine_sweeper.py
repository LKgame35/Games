import random

r0=["#","#","#","#","#",]
r1=["#","#","#","#","#",]
r2=["#","#","#","#","#",]
r3=["#","#","#","#","#",]
r4=["#","#","#","#","#",]
r=[r0,r1,r2,r3,r4]
for i in range(10):
    rand1=random.randint(0,4)
    rand2=random.randint(0,4)
    # print(rand1)
    # print(rand2)
    rand11=random.randint(0,4)
    rand22=random.randint(0,4)
    # print(rand11)
    # print(rand22)
    if rand1!=rand11 or rand2!=rand22:
        break


for ii in range(25):
    z=0
    print("\n    0 1 2 3 4\n")
    for i in range(5):
        print(str(i)+"   "+(' '.join(r[i])))
    print("Ievadiet 777, lai minētu atbildi. ")
    g1=int(input("\n \nY ass "))
    if g1==777:
        a=int(input("Ievadiet mīnas atrašanās Y koordināti. "))
        b=int(input("Ievadiet mīnas atrašanās X koordināti. "))
        c=int(input("Ievadiet mīnas atrašanās Y koordināti. "))
        d=int(input("Ievadiet mīnas atrašanās X koordināti. "))
        if a==rand1 and b==rand2 or a==rand11 and b==rand22 :
            if c==rand1 and d==rand2 or c==rand11 and d==rand22 :
                print("Uzvara!")
                break
        else: print("Nepareizi! ")
        break
    g2=int(input("X ass "))

    if rand1==g1 and rand2==g2 or rand11==g1 and rand22==g2:
        print("Game over!")
        break
    for i in range(3):
        if g1==rand1 and g2-1+i==rand2 or g1-1==rand1 and g2-1+i==rand2 or g1+1==rand1 and g2-1+i==rand2:
            z+=1
        # if g1-1==rand1 and g2-1+i==rand2:
        #     z+=1
        # if g1+1==rand1 and g2-1+i==rand2:
        #     z+=1
        if g1==rand11 and g2-1+i==rand22 or g1-1==rand11 and g2-1+i==rand22 or g1+1==rand11 and g2-1+i==rand22:
            z+=1
        # if g1-1==rand11 and g2-1+i==rand22:
        #     z+=1
        # if g1+1==rand11 and g2-1+i==rand22:
        #     z+=1

    r[g1][g2]=str(z)