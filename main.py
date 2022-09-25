from  datetime import datetime, timedelta
import configparser
import pyautogui
import time

config = configparser.ConfigParser()
config.read('config.ini')
dk_start = config['SERVER_LINKS']['dk_start']
dk_server = config['SERVER_LINKS']['dk_server']
speed = config['MAIN']['speed_click']
pyautogui.PAUSE = float(speed)

screen_size_x, screen_size_y = pyautogui.size()

if screen_size_x == 1920 and screen_size_y == 1080:

    with open('accounts.txt') as file:
        while (line := file.readline().rstrip()):
            account = line.split(':')
            servers = account[2].split('.')

            # Login...
            pyautogui.click(580, 820)
            pyautogui.write(account[0])
            pyautogui.click(580, 880)
            pyautogui.write(account[1])
            pyautogui.click(500, 945)


            for server in servers:
                # Load server
                pyautogui.click(625, 55)
                pyautogui.write(dk_server.replace(':server:', server))
                pyautogui.press('enter')

                # Check Loading
                start_time = datetime.now()
                finish_time = start_time + timedelta(seconds=25)
                loading = 0

                while start_time < finish_time:
                    hearts_image = pyautogui.locateOnScreen('images/hearts.png', confidence=0.7)
                    start_time = datetime.now()
                    if hearts_image:
                        loading = 1
                        break

                # Actions
                if loading:
                    # Waiting
                    time.sleep(2)

                    # Flowers
                    pyautogui.click(hearts_image)
                    pyautogui.click(1050, 720)
                    pyautogui.click(1200, 720)
                    time.sleep(1)
                    pyautogui.click(1880, 130)
                    time.sleep(1)

                    # Daily
                    #image = "images/first.png"
                    #button = pyautogui.locateOnScreen(image, confidence=0.7)
                    pyautogui.click(1800, 210)
                    pyautogui.click(580, 520)
                    pyautogui.click(840, 320)
                    pyautogui.click(820, 500)
                    pyautogui.click(900, 720)
                    pyautogui.click(1000, 320)
                    pyautogui.click(900, 440)
                    pyautogui.click(920, 630)

                    # Close tab
                    pyautogui.click(240, 15)

            # Go start page...
            pyautogui.click(625, 55)
            pyautogui.write(dk_start)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.click(500, 840)
else:
    print("Error display")

input('Press ENTER to exit')