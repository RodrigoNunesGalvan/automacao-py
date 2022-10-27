import pyautogui
from time import sleep

with open('convertcsv.csv','r') as arquivo:
    for linha in arquivo:
        numero = linha.split(',')[0]
        
        pyautogui.doubleClick(649,349,duration=0.2)
        pyautogui.write(numero)

        pyautogui.click(827,344,duration=0.5)

        pyautogui.doubleClick(928,487,duration=1.8)
        pyautogui.hotkey('ctrl', 'c') 
      
        pyautogui.doubleClick(1092,86,duration=0.2)
       
        # with open('convertcsv.csv','a') as arquivo:
        #     for linha in arquivo:
        #         sequence = linha.split(',')[1]
        #         pyautogui.write(status)

        # pyautogui.hotkey('ctrl', 'v')
        # pyautogui.hotkey('down')
        pyautogui.click(1253,141,duration=0.1)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(',')
       
        sleep(0.2)


# try:
#     while True:
#         x,y = pyautogui.position()
#         positionStr = 'x: ' + str(x).rjust(4) + 'y: ' + str(y).rjust(4)
#         print(positionStr)


# except KeyboardInterrupt:
#     print('\nDone')