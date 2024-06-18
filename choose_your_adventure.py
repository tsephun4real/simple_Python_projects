name=input("type your name: ")
print("welcome", name, " to this adventure!!")

answer=input("you are on adirt road, it has come to an end and you can go left or right. which way would you like to go?  ").lower()

if answer=="left":
    answer=input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim across: ")

    if answer=="swim":
        print("you swam across and were eaten by an alligatior!")

    elif answer=="walk":
        print("you walked for many miles, ran out of water and you lost the game")

    else:
        print('not a valid option. you lose.' )        

elif answer=="right":
    answer=input("you come to a bridge , it looks wobbly, do you want to cross it or head back (cross/back)?   ")

    if answer=="back":
        print("You go back and lose the game")
    elif answer=="cross":
        answer=input("you cross the bridge and meet an stranger. Do you talk to them(yes/no)? ")
        if  answer=="yes":
            print("you talk to stranger and they give you gold and YOU WIN!!")

        elif answer=="no":
            print("You ignore the stranger and they are offended and you lose!!")

        else:
             print('not a valid option. you lose.' )   

                
        
    else:
        print('not a valid option. you lose.' )   

    
else:
    print("not a valid option. You lose.")        

print("Thank you for trying",name)