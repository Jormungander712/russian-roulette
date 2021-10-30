import random
import keyboard
import time

#setup
places = ["1" , "2" , "3" , "4" , "5" , "6"]
bullet_place = random.choice(places)
position = 1
haha = 4
dead = False
#game
print("Player 1's turn. (press a)")
while haha < 5:
    if keyboard.is_pressed("a"):
        haha = 5
        if bullet_place == "1":
            if position == 1:
                print("You died, F")
                dead = True
            else:
                print("You survived!")
                position = position + 1
        else:
            print("You survived!")
            position = position + 1
if dead == False:
    time.sleep(2)
    haha = 4
    print("Player 2's turn.")
    while haha < 5:
        if keyboard.is_pressed("a"):
            haha = 5
            if bullet_place == "2":
                if position == 2:
                    print("You died, F")
                    dead = True
                else:
                    print("You survived!")
                    position = position + 1
            else:
                print("You survived!")
                position = position + 1
    if dead == False:
        time.sleep(2)
        haha = 4
        print("Player 1's turn.")
        while haha < 5:
            if keyboard.is_pressed("a"):
                haha = 5
                if bullet_place == "3":
                    if position == 3:
                        print("You died, F")
                        dead = True
                    else:
                        print("You survived!")
                        position = position + 1
                else:
                    print("You survived!")
                    position = position + 1
        if dead == False:
            time.sleep(2)
            haha = 4
            print("Player 2's turn.")
            while haha < 5:
                if keyboard.is_pressed("a"):
                    haha = 5
                    if bullet_place == "4":
                        if position == 4:
                            print("You died, F")
                            dead = True
                        else:
                            print("You survived!")
                            position = position + 1
                    else:
                        print("You survived!")
                        position = position + 1
            if dead == False:
                time.sleep(2)
                haha = 4
                print("Player 1's turn.")
                while haha < 5:
                    if keyboard.is_pressed("a"):
                        haha = 5
                        if bullet_place == "5":
                            if position == 5:
                                print("You died, F")
                                dead = True
                            else:
                                print("You survived!")
                                position = position + 1
                        else:
                            print("You survived!")
                            position = position + 1
                if dead == False:
                    time.sleep(2)
                    haha = 4
                    print("Player 2's turn.")
                    while haha < 5:
                        if keyboard.is_pressed("a"):
                            haha = 5
                            if bullet_place == "6":
                                if position == 6:
                                    print("You died, F")
                                    dead = True
                                else:
                                    print("You survived!")
                                    position = position + 1
                            else:
                                print("You survived!")
                                position = position + 1
                    if dead == False:
                        print("How?")