import os

beigas=0
rinda6=[".", ".",".",".",".",".",".",]
rinda5=[".", ".",".",".",".",".",".",]
rinda4=[".", ".",".",".",".",".",".",]
rinda3=[".", ".",".",".",".",".",".",]
rinda2=[".", ".",".",".",".",".",".",]
rinda1=[".", ".",".",".",".",".",".",]

laukums=[rinda6, rinda5,rinda4,rinda3,rinda2,rinda1]

for big in range(42):

    print("\n0 1 2 3 4 5 6")
    for i in range(6):
        print(' '.join(laukums[i]))
    
    if beigas==1:
        break

    if int(big)%2==0:speletajs="#"
    else: speletajs="@"

    gajiens=int(input(f"Izvēlieties lauciņu spēlētājs {speletajs}.  "))

    for i in range(6):

        if laukums[5-int(i)][gajiens]==".":
            laukums[5-int(i)][gajiens]=speletajs
            z=5-int(i)
            break
    for iii in range(3):
        for ii in range(4):
            c1=0
            c2=0
            for i in range(4):
                # no kreisas uz labo dilstosa diognale
                if laukums[i+iii][i+ii]==speletajs:
                    c1=c1+1
                if c1==4: 
                    beigas=1
                # no kreisas uz labo augosa diognale
                if laukums[5-i-iii][i+ii]==speletajs:
                    c2=c2+1
                if c2==4: 
                    beigas=1

    for iii in range(6):
        for ii in range(4):
            c3=0
            for i in range(4):
                # horizontali no augsas uz leju
                if laukums[iii][i+ii]==speletajs:
                    c3=c3+1
                if c3==4: 
                    beigas=1
    for iii in range(6):
        for ii in range(3):
            c4=0
            for i in range(4):
                # vertikali no augas uz leju
                if laukums[i+ii][iii]==speletajs:
                    c4=c4+1
                if c4==4: 
                    beigas=1
    os.system('cls')

print(f"Uzvarēja spēlētājs {speletajs}  ")
