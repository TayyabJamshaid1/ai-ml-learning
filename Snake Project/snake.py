import random
'''
snake   1
water  -1
gun    0
'''
computer=random.choice([1,-1,0])
userDicStr=input("Enter your choice : ")
userDic={"w":-1,"g":0,"s":1}
reverseDic={-1:"water",0:"gun",1:"snake"}
you=userDic[userDicStr]
print(f"You choose {reverseDic[you]} , computer choose {reverseDic[computer]}")

if (computer==you):
    print("Game is draw")
else:
    if (computer==1) and (you==-1):
        print("You loose")
    elif (computer==1) and (you==0):
        print("You win")
    elif (computer==0) and (you==1):
        print("You loose")
    elif (computer==0) and (you==-1):
        print("You win")
    elif (computer==-1) and (you==1):
        print("You win")
    elif (computer==-1) and (you==0):
        print("You loose")
    else : print("Something went wrong")