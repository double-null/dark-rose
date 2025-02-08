from datetime import datetime, timedelta

from helpers.monolog import Monolog
from helpers.site import Site
from helpers.image import Image

import pyautogui
import time
import components

config = components.load_config()
actions = config['actions']

pyautogui.FAILSAFE = False
pyautogui.PAUSE = float(config['speed'])

image = Image()
monolog = Monolog()

print("VERSION: 1.2.1")

screen_size_x, screen_size_y = pyautogui.size()
if screen_size_x == 1920 and screen_size_y == 1080:

    site = Site()

    with open('accounts.txt') as file:
        while (line := file.readline().rstrip()):
            data = line.split(':')
            servers = data[2].split('.')

            # Login...
            auth = site.login(data[0], data[1])

            if (auth):
                for server in servers:
                    # Load server
                    pyautogui.click(625, 55)
                    pyautogui.write(config['dk_server'].replace(':server:', server))
                    pyautogui.press('enter')

                    # Check Loading
                    start_time = datetime.now()
                    finish_time = start_time + timedelta(seconds=25)
                    loading = 0

                    while start_time < finish_time:
                        try:
                            cryptIcon = pyautogui.locateOnScreen(
                                "images/alchemy.png",
                                region=(900, 90, 1600, 300),
                                confidence=0.7
                            )
                            loading = 1
                            break
                        except pyautogui.ImageNotFoundException:
                            start_time = datetime.now()
                            continue

                    # Actions
                    if loading:
                        # Waiting
                        time.sleep(2)

                        if int(actions['flowers']) == 1:
                            try:
                                hearts_image = pyautogui.locateOnScreen('images/hearts.png', confidence=0.7)
                                pyautogui.click(hearts_image)
                                pyautogui.click(1050, 720)
                                pyautogui.click(1200, 720)
                                time.sleep(1)
                                pyautogui.click(1880, 130)
                                time.sleep(1)
                            except pyautogui.ImageNotFoundException:
                                print('Flowers failed')



                        if int(actions['daily']) == 1:
                            pyautogui.click(1800, 210)
                            pyautogui.click(580, 520)

                            if (pyautogui.pixel(1200, 710) == (78, 18, 0)) :
                                pyautogui.click(1225, 700)

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
                            cryptIcon = image.search("images/crypt.png",(1200, 90, 1600, 150))

                            if (cryptIcon != None) :
                                pyautogui.click(cryptIcon)
                                time.sleep(0.5)

                                # Get reward
                                rewardBtnColor = pyautogui.pixel(880, 525)
                                if rewardBtnColor[1] > 90:
                                    pyautogui.click(880, 525)
                                    time.sleep(3)

                                # Install crypt
                                blitzBtnColor = pyautogui.pixel(1280, 625)
                                cancelBlitzBtnColor = pyautogui.pixel(1260, 520)
                                if (blitzBtnColor[1] > 90 and cancelBlitzBtnColor[0] < 200):
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

                                    if (command[0] == 'double'):
                                        pyautogui.doubleClick(int(command[1]), int(command[2]))

                                    if (command[0] == 'write'):
                                        pyautogui.write(command[1])

                                    if (command[0] == 'wait'):
                                        time.sleep(int(command[1]))

                                    if (command[0] == 'image'):
                                        try:
                                            image = pyautogui.locateOnScreen('images/' + command[1], confidence=0.7)
                                            pyautogui.click(image)
                                        except pyautogui.ImageNotFoundException:
                                            print('Image', command[1], 'not found')

                        monolog.log('done', data[0] + ' ' + server)

                    else:
                        if (pyautogui.pixel(110, 170) == (6, 102, 18)) :
                            error = 'LOW LEVEL '+ data[0] + '(' + server + ')'
                            monolog.log('fails', error)

                # Logout
                site.logout()
else:
    print("Error display")

input("Press ENTER to exit")