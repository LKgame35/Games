pirma=["-","-","-"]
otra=["-","-","-"]
tresa=["-","-","-"]
speletajs=["X", "O","X", "O","X", "O","X", "O","X", "O","X", "O","X", "O","X", "O","X", "O","X", "O","X", "O","X", "O",]


for i in range(9):

    print(pirma[0]+pirma[1]+pirma[2])
    print(otra[0]+otra[1]+otra[2])
    print(tresa[0]+tresa[1]+tresa[2])
    print("Gājiens "+ speletajs[i])
    a=int(input("Y "))
    b=int(input("X "))
    print("\n \n \n \n")
    b=b-1
    if a==1:
        pirma[b]=speletajs[i]
    if a==2:
        otra[b]=speletajs[i]
    if a==3:
        tresa[b]=speletajs[i]



    if pirma[0]==speletajs[i] and pirma[1]==speletajs[i] and pirma[2]==speletajs[i] or otra[0]==speletajs[i] and otra[1]==speletajs[i] and otra[2]==speletajs[i] or tresa[0]==speletajs[i] and tresa[1]==speletajs[i] and tresa[2]==speletajs[i]:
        print(f"\n Uzvara speletajam {speletajs[i]}! ")
        break

    # if pirma[0]==speletajs[i] and pirma[1]==speletajs[i] and pirma[2]==speletajs[i]:
    #     print(f"\n Uzvara speletajam {speletajs[i]}! ")
    #     break
    # if otra[0]==speletajs[i] and otra[1]==speletajs[i] and otra[2]==speletajs[i]:
    #     print(f"\n Uzvara speletajam {speletajs[i]}! ")
    #     break
    # if tresa[0]==speletajs[i] and tresa[1]==speletajs[i] and tresa[2]==speletajs[i]:
    #     print(f"\n Uzvara speletajam {speletajs[i]}! ")
    #     break


    if pirma[0]==speletajs[i] and otra[0]==speletajs[i] and tresa[0]==speletajs[i]:
        print(f"\n Uzvara speletajam {speletajs[i]}! ")
        break
    if pirma[1]==speletajs[i] and otra[1]==speletajs[i] and tresa[1]==speletajs[i]:
        print(f"\n Uzvara speletajam {speletajs[i]}! ")
        break
    if pirma[2]==speletajs[i] and otra[2]==speletajs[i] and tresa[2]==speletajs[i]:
        print(f"\n Uzvara speletajam {speletajs[i]}! ")
        break
    
    if pirma[0]==speletajs[i] and otra[1]==speletajs[i] and tresa[2]==speletajs[i]:
        print(f"\n Uzvara speletajam {speletajs[i]}! ")
        break
    if pirma[2]==speletajs[i] and otra[1]==speletajs[i] and tresa[0]==speletajs[i]:
        print(f"\n Uzvara speletajam {speletajs[i]}! ")
        break

print(pirma[0]+pirma[1]+pirma[2])
print(otra[0]+otra[1]+otra[2])
print(tresa[0]+tresa[1]+tresa[2])