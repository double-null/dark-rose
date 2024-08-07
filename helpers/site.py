import pyautogui, time
from helpers.config import Config

class Site:

    def __init__(self):
        self.startPageUrl = Config().getLink('dk_start')

    def toStartPage(self):
        pass

    def login(self, username, password):
        sec = 0
        while (sec < 20):

            if (pyautogui.pixel(500, 940) == (51, 122, 183)):
                pyautogui.click(580, 820)
                pyautogui.write(username)
                pyautogui.click(580, 880)
                pyautogui.write(password)
                pyautogui.press('enter')

                if (pyautogui.pixel(500, 850) == (51, 122, 183)):
                    return True
                else:
                    return False

            sec = sec + 2
            time.sleep(2)

        return False

    def logout(self):
        pyautogui.click(625, 55)
        pyautogui.write(self.startPageUrl + '/user/logout')
        pyautogui.press('enter')