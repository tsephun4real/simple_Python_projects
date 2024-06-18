import random
top_of_range=input("Type a number:  ")


if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print('please type anumber larger than 0 next tiem.')
        quit()

else:
    print('please type a number next time: ')
    quit()

random_num=random.randint(0,top_of_range)          
guesses=0    
while True:
    guesses+=1
    user_guess=input("Make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print('please type a number next time: ')
        continue


    if user_guess==random_num:
        print('You got it!')
        break
    elif user_guess>random_num:
        print('you were above the number!')
        continue
    else:
        print('You were below the number!')    

print('you got it in',guesses,'guesses')           

   
