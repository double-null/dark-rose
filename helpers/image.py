import pyautogui as pg

class Image:

    def search(self, imagePath, region):
        try:
            icon = pg.locateOnScreen(imagePath, region=region, confidence=0.7)
            return icon
        except Exception as e:
            print(f"Unexpected {e=}, {type(e)=}")
            return None