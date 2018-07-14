import pyautogui
import keyboard
import threading
import time

class ClickerSolver:

    def __init__(self):

        #each value in the array is a tuple. X coord, Y coord, timing T (seconds)
        #Format: ((x, y), T)
        self.clickLocationTimings = []

    #puts responsibility to add click locations to user.
    def easySetClickLocations(self):
        print("Mouse over areas you want to click and press A on your keyboard to add them. When Finished, press Q to exit.")
        isPressingKey = False
        clickTime = 1
        while True:
            if keyboard.is_pressed('q'): #end input
                break
            if keyboard.is_pressed('a') and (not isPressingKey):
                #add to click list. Assume 0 wait time between clicking.
                self.clickLocationTimings.append((pyautogui.position(), clickTime))
                print("Area Added!")
                isPressingKey = True

            if keyboard.is_pressed('w') and (not isPressingKey):
                clickTime += 1
                print("Clicktime: " + str(clickTime))
                isPressingKey = True

            if keyboard.is_pressed('s') and (not isPressingKey) and clickTime != 1:
                clickTime -= 1
                print("Clicktime: " + str(clickTime))
                isPressingKey = True

            if not (keyboard.is_pressed('a') or keyboard.is_pressed('w') or keyboard.is_pressed('s')): #one location added per keypress
                isPressingKey = False

    #loops through click locations until user exits
    def easyStart(self):
        cont = True
        print("STARTING PROGRAM. PRESS Q TO QUIT")
        while cont:
            for xy in self.clickLocationTimings:
                x, y = xy[0]
                pyautogui.click(x, y)
                if keyboard.is_pressed('q'): #quit keyboard input
                        print('Program Ended!')
                        cont = False #exit while
                        break #exit for loop


    #individual threads based on click timings
    #clickTuple Format: ((x,y), timing)
    def timedStart(self):
        counter = 0
        cont = True
        while cont:
            time.sleep(0.10)
            counter += 1
            for clickLocation in self.clickLocationTimings:
                x, y = clickLocation[0]
                timing = clickLocation[1]

                #interval timings
                #1 = every time
                #2 = every other time
                #3 = every third time, etc.
                #uses counter variable to keep track of this
                if counter%timing == 0:
                    pyautogui.click(x, y)
                    
                if keyboard.is_pressed('q'): #quit keyboard input
                        print('Program Ended!')
                        cont = False #exit while
                        break #exit for loop

    
                
clkr = ClickerSolver()
clkr.easySetClickLocations()
clkr.timedStart()
#clkr.easyStart()
