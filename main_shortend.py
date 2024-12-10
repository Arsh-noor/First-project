import random
'''
1 for Snake
-1 for Water
0 for Gun
'''

computer = random.choice([-1 , 0 , 1])
youstr = input("Enter your choice: ")
youDict = {"s": 1 , "w": -1 , "g": 0}
reverseDict = {1:"snake",-1:"water" ,0: "gun"}
you = youDict[youstr]

print(f"You chose {reverseDict[you]} \n Computer chose {reverseDict[computer]}")

if (computer==you):
    print("It's a Draw ^^)")

else:

 '''
    if (computer == -1 and you == 1): (computer - you) = -2
        print("You win! :)")

    elif (computer == -1 and you == 0):(computer - you) = -1
        print("You lose! :(")

    elif (computer == 1 and you == -1): (computer - you) = 2
        print("You lose! :(")

    elif (computer == 1 and you == 0): (computer - you) = 1
        print("You win! :)")

    elif (computer == 0 and you == 1): (computer - you) = -1
        print("You win! :)")

    elif (computer == 0 and you == -1): (computer - you) = 1
        print("You lose! :(") 
        
     The below logic is written on the logic of computer - you   

'''
if((computer-you)== -1 or (computer-you)== 2 ):
    print("You lose! :(")

else :
        print("You win! :)")