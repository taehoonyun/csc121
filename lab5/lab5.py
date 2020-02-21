




def main():

    canteen_num = 0
    speed=1
    distance =0
    total_distance =60
    done = False
    thirsty = 0
    tired = 0


   

    while done == False:
        

        print("A. Drink from your canteen. \n")
        print("B. Ahead moderate speed. \n")
        print("C. Ahead full speed. \n")
        print("D. Stop and rest. \n")
        print("E. Status check.\n")
        print("Q. Quit.\n")
        
        key = input("Your choice? \n")
        
        #Variable about thirsty for every ten streets
        tired = distance
        
        #stop to drink
        if key == "A":
            canteen_num += 1
            thirsty = thirsty-2
            speed =0
        
        elif key == "B":
            speed += 5
            distance +=speed/4
            print("\n Miles traveled : ",distance,"\n")
            
        
        elif key == "C":
            speed += 10
            distance +=speed/4
            print("\n Miles traveled :",distance,"\n")
            
        #rest
        elif key == "D":
            print("\n have a good time!")
            print("Zzzz\n")
            thirsty =0
            speed =0
        
        elif key == "E":
            print("\n Miles traveled :",distance)
            print("Drinks in canteen : ",canteen_num)
            print("The locals are ",total_distance-distance,"miles behind you.\n")
        
        #This keeps it thirsty.... and warning... should I make this a func??    
            thirsty -=1

        elif key=="Q":
            quit = input("Do you want to quit?")
            if quit == "y":
                done = True 
        else:
            print("please press another key.\n\n")
        
        if tired > 5:
            thirsty +=1
            tired =0
        
        if thirsty == 5:
            print("===============================================")
            print("===================WARNING===================== \n")
            print("He needs some water!! \n")
        
        if thirsty == 7 and distance >= total_distance:
            print("--He dead--")
            print("--------------------game over----------------------")
            done = True
            return done

        if distance >= total_distance :
            print(" He found an oasis!! ")
            print("===================clear=================")
            done = True




if __name__ == "__main__":     
    main()