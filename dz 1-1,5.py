import random
random_number = random.randint(1,10)
player_choise = (int(input("угадайте число от 1 до 10")))
while player_choise != random_number:
    if player_choise==random_number:
        print ("вы угадали!")
    else:
        if player_choise>random_number:
            print ("меньше")
            player_choise = (int(input("угадайте число от 1 до 10")))
            if player_choise==random_number:
                print ("вы угадали!")        
        else:
            print ("больше")
            player_choise = (int(input("угадайте число от 1 до 10")))
            if player_choise==random_number:
                print ("вы угадали!")
