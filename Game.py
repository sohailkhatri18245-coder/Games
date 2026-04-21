import random
pointA=0
pointB=0
i=0
game = int(input("Press 1 for stone paper scissor and 2 for Dice roll : "))
if game == 1:
    options = ["Scissor","Stone","Paper"]
    for j in range(len(options)):
        print(options[j],":",j)

    
    while (i<=10):
        chooce=int(input("Enter your choice to play the game:"))
        SS=random.choice(options)
        if chooce >=0 and chooce<=2:
            if SS== options[chooce]:
                print("Match tied\n")  
                        

            else:
                if SS== "Scissor" and options[chooce]=="Paper":
                    print("You chose",options[2],"You Have Loss and Opponent Win because he choose.",SS,"\n")
                    pointB+=1
                elif SS== "Stone" and options[chooce]=="Paper":
                    print("You chose",options[2],"You Have Win and Opponent Loose because he choose.",SS,"\n")
                    pointA+=1
                elif SS== "Paper" and options[chooce]=="Scissor":
                    print("You chose",options[0],"You Have Win and Opponent Loss because he choose.",SS,"\n")
                    pointA+=1
                elif SS== "Stone" and options[chooce]=="Scissor":
                    print("You chose",options[0],"You Have loss and Opponent Win because he choose.",SS,"\n")
                    pointB+=1
                elif SS== "Scissor" and options[chooce]=="Stone":
                    print("You chose",options[1],"You Have win and Opponent loss because he choose.",SS,"\n")
                    pointA+=1
                elif SS== "Paper" and options[chooce]=="Stone":
                    print("You chose",options[1],"You Have loss and Opponent Win because he choose.",SS,"\n")
                    pointB+=1
                else:
                    print("Press Valid Numbers")
                
                
        else:
            print("\nHey bro read the upper message again\n")
            pass    
        i=i+1
    print("oponent points Points:",pointB)
    print("Your Points:",pointA)


elif game == 2:

    dice =[0,1,2,3,4,5,6]
    while (i<=10):
        choice=int(input("Enter your choice to play the game:"))
        if choice<=6 and choice >0:
            if random.randint(1,6)== dice[choice]:
                print("You Won🫡 🫡 🫡 🫡\n")
                pointA+=1
                
            else:
                print("You Have Loss. Try Again 😢 😢 😢 😢\n")
                pointB+=1
        else:
            print("You can choose only 1 to 6 number")
            pass
        i+=1
    print("Opponent points :",pointB)
    print("Your Points:",pointA)
