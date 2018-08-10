import pyautogui
import keyboard
import threading
import time

class ClickerSolver:

    def __init__(self):

        #each value in the array is a tuple. X coord, Y coord, timing T (seconds)
        #Format: ((x, y), Timing)
        self.clickLocationTimings = []

        #Format: ((x1, y1), (x2, y2), DragTime, Timing)
        self.dragLocationTimings = []

    #puts responsibility to add click locations to user.
    def easySetClickLocations(self):
        print("Mouse over areas you want to click and press A on your keyboard to add them.")
        print("Use W and S to adjust the timings.")
        print("When Finished, press Q to exit.")
        isPressingKey = False
        clickTime = 1
        while True:
            if keyboard.is_pressed('q'): #end input
                break
            
            if keyboard.is_pressed('a') and (not isPressingKey):
                #add to click list.
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

    #loops through click locations until user exits, no timings
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


    #adding click and drag locations + timings to gui checker.
    #format is ((x1, y1), (x2, y2), Dragtime, Timing)
    def setDragLocations():
        print("Mouse over start/end areas you want to click and press A/D on your keyboard to add them.")
        print("Use W and S to adjust the timings.")
        #TODO: Implement properly
        #print("Use +/- to adjust the drag times")
        print("Use E to add a complete click drag location to the list")
        print("When Finished, press Q to exit.")
        xyone, xytwo, = pyautogui.position()
        dragtime, timing = 1 #default drag timing and click timing
        isPressingKey = False
        while cont:
            if keyboard.is_pressed('q'): #end input
                break

            #drag start location
            if keyboard.is_pressed('a') and (not isPressingKey):
                #add to drag start list.
                xyone = pyautogui.position()
                print("Start Postion: " + str(xyone))
                isPressingKey = True

            #drag end location
            if keyboard.is_pressed('d') and (not isPressingKey):
                xytwo = pyautogui.position()
                print("End Position: " + str(xytwo))
                isPressingKey = True

            if keyboard.is_pressed('w') and (not isPressingKey):
                timing += 1
                print("Timing: " + str(clickTime))
                isPressingKey = True

            if keyboard.is_pressed('s') and (not isPressingKey) and clickTime != 1:
                timing -= 1
                print("Timing: " + str(clickTime))
                isPressingKey = True

            if keyboard.is_pressed('e') and (not isPressingKey):
                self.dragLocationTimings.append((xyone, xytwo, dragtime, timing))
                
            #one location added per keypress
            if not (keyboard.is_pressed('a') or keyboard.is_pressed('w')
                    or keyboard.is_pressed('s') or keyboard.is_pressed('d')
                    or keyboard.is_pressed('e')):
                isPressingKey = False
            
        
        

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
