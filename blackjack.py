import random
import time

#print (random.randint(1,12))
username = ("None")
value = ("None")
rolls = 1
user_numbers = [0]
house_numbers = [0]

username = input("Please input your username: ")

while rolls < 6:
    # Player Starts the game
    print ("Go or stop?")
    choice = input()
    
    if choice == "go":
        value = (random.randint(1,12))
        user_numbers.append(value)
        value = str(value)
        rolls_str = str(rolls)
        print ("Round "+ rolls_str)
        print ("You rolled a "+value)
        print (user_numbers)
        check_total = sum(user_numbers)
        check_total_str = str(check_total)
        rolls = (rolls + 1)
        #Checking if the number is over 21
        
        if check_total > 21:
            print ("You have exceeded 21. House wins")
            print ("Final total is "+ check_total_str)
            break
    
    #Player stoping the game
    elif choice == "stop":
        total = sum(user_numbers)
        total = str(total)
        print ("your total is "+ total)

        #Houses turn
        house_value = (random.randint(1,12))
        house_numbers.append(house_value)
        house_value = str(house_value)
        print ("----------------------------")
        print ("House got a "+ house_value)
        print (house_numbers)
        house_check_total = sum(house_numbers)
        house_check_total_str = str(house_check_total)

        if house_check_total > 21:
            print ("The house have exceeded 21. You win!")
            print ("House final total is "+ house_check_total_str)
            f = open("highscore.txt", "a")
            f.write(username+ " : "+ total+"\n")
            f.close()
            break

        else:
            house_total = sum(house_numbers)
            house_total_str = str(house_total)
            user_total = sum(user_numbers)
            user_total_str = str(user_total)
            print (max(user_total_str))
            print (max(house_total_str))

            #if house_total 



    #Houses turn
    house_value = (random.randint(1,12))
    house_numbers.append(house_value)
    house_value = str(house_value)
    print ("----------------------------")
    print ("House got a "+ house_value)
    print (house_numbers)
    house_check_total = sum(house_numbers)
    house_check_total_str = str(house_check_total)

    if house_check_total > 21:
        print ("The house have exceeded 21. You win!")
        print ("House final total is "+ house_check_total_str)
        f = open("highscore.txt", "a")
        f.write(username+ " : "+ total+"\n")
        f.close()
        break