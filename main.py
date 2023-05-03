from  datetime import datetime, timedelta
import configparser
import pyautogui
import time

config = configparser.ConfigParser()
config.read('config.ini')
dk_start = config['SERVER_LINKS']['dk_start']
dk_server = config['SERVER_LINKS']['dk_server']
speed = config['MAIN']['speed_click']
actions = config['ACTIONS']
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

                    if int(actions['flowers']) == 1:

                        pyautogui.click(hearts_image)
                        pyautogui.click(1050, 720)
                        pyautogui.click(1200, 720)
                        time.sleep(1)
                        pyautogui.click(1880, 130)
                        time.sleep(1)

                    if int(actions['daily']) == 1:
                        #image = "images/first.png"
                        #button = pyautogui.locateOnScreen(image, confidence=0.7)
                        pyautogui.click(1800, 210)
                        pyautogui.click(580, 520)

                        # 2 Tab
                        secondTabColor = pyautogui.pixel(777, 320)
                        if (secondTabColor != (44, 44, 44)): # active (not gray)
                            pyautogui.click(730, 325)
                            pyautogui.click(785, 795)
                            pyautogui.click(910, 645)

                        # 3 Tab
                        thirdTabColor = pyautogui.pixel(900, 320)
                        if (thirdTabColor != (65, 18, 12)):  # lvl up
                            time.sleep(4)

                        pyautogui.click(840, 320)
                        todayBtnColor = pyautogui.pixel(870, 495)

                        if (todayBtnColor != (143, 0, 0)) : # not red
                            pyautogui.click(820, 500)

                        fiveDaysBtnColor = pyautogui.pixel(930, 710)
                        if (fiveDaysBtnColor != (56, 56, 56)) : # active
                            pyautogui.click(900, 720)

                        # 4 Tab
                        pyautogui.click(1000, 320)
                        pyautogui.click(900, 440)
                        pyautogui.click(920, 630)

                        cancelBtnColor = pyautogui.pixel(980, 640)
                        if cancelBtnColor[0] == 0 and cancelBtnColor[1] > 60 :
                            pyautogui.click(980, 640)

                        pyautogui.click(1430, 285)

                    if int(actions['mailbox']) == 1:
                        pyautogui.click(1775, 160)
                        pyautogui.click(790, 755)
                        pyautogui.click(1080, 755)

                    if int(actions['crypt']) == 1:
                        # Start crypt
                        cryptIcon = pyautogui.locateOnScreen(
                            "images/crypt.png",
                            confidence=0.7
                        )
                        pyautogui.click(cryptIcon)
                        time.sleep(0.5)

                        # Get reward
                        rewardBtnColor = pyautogui.pixel(880, 525)
                        if rewardBtnColor[1] > 90 :
                            pyautogui.click(880, 525)
                            time.sleep(3)

                        # Install crypt
                        blitzBtnColor = pyautogui.pixel(1280, 625)
                        cancelBlitzBtnColor = pyautogui.pixel(1260, 520)
                        if (blitzBtnColor[1] > 90 and cancelBlitzBtnColor[0] < 200) :
                            pyautogui.click(1240, 640)
                            pyautogui.doubleClick(970, 480)
                            pyautogui.write('99')
                            pyautogui.click(1000, 525)
                            pyautogui.click(900, 640)

                        # Close crypt
                        pyautogui.click(1315, 320)


                    if int(actions['custom']) == 1:
                        with open('custom.txt') as custom_file:
                            while (line := custom_file.readline().rstrip()):
                                command = line.split(' ')

                                if (command[0] == 'click'):
                                    pyautogui.click(int(command[1]), int(command[2]))

                                if (command[0] == 'wait'):
                                    time.sleep(int(command[1]))

                                if (command[0] == 'image'):
                                    image = pyautogui.locateOnScreen('images/' + command[1], confidence=0.7)
                                    pyautogui.click(image)

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