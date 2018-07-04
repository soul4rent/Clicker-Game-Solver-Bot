import pyautogui
import keyboard
import threading

class ClickerSolver:

    def __init__(self):

        #each value is a tuple. X coord, Y coord, timing T (seconds)
        #Format: ((x, y), T)
        #can't use dictionary since coords not guaranteed to be unique
        self.clickLocationTimings = []

    #puts responsibility to add click locations to user.
    def easySetClickLocations(self):
        print("Mouse over areas you want to click and press A on your keyboard to add them. When Finished, press Q to exit.")
        isPressingKey = False
        while True:
            if keyboard.is_pressed('q'): #end input
                break
            if keyboard.is_pressed('a') and (not isPressingKey):
                #add to click list. Assume 0 wait time between clicking.
                self.clickLocationTimings.append((pyautogui.position(), 0))
                print("Area Added!")
                isPressingKey = True

            if not keyboard.is_pressed('a'): #one location added per keypress
                isPressingKey = False

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
        
        
clkr = ClickerSolver()
clkr.easySetClickLocations()
clkr.easyStart()
