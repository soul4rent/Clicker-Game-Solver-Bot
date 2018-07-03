import pyautogui
import keyboard



clickAreas = []
isPressingKey = False #used to prevent keyspam during input
print("Welcome to clicker solver! Please highlight areas you want to click and press A on your keyboard to add them! When ready, press S to start the program!")
while True:
    
    if keyboard.is_pressed('s'): #start program
        break
    if keyboard.is_pressed('a') and (not isPressingKey): #add to click list
        clickAreas.append(pyautogui.position())
        print("Area Added!")
        isPressingKey = True

    if not keyboard.is_pressed('a'): #help prevnt click spam
        isPressingKey = False
        
        
cont = True
print("STARTING PROGRAM. PRESS Q TO QUIT")
while cont:
    for xy in clickAreas:
        x, y = xy
        pyautogui.click(x, y)
        if keyboard.is_pressed('q'): #quit keyboard input
                print('Program Ended!')
                cont = False
                break #end loop
    
