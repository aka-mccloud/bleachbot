import os

from sikuli import *

class BleachApp:
    def __init__(self):
        self._app = None
        self._url = None
        self._urlPattern = Pattern("1540071070819-1.png").targetOffset(25,0)

    def open(self):
        self._url = os.popen('/home/tuser/flashplayer/bleach.py').read().strip()
        self._app = App.open('/home/tuser/flashplayer/flashplayer')
        sleep(1)
    
        with Region(self._app.window()):
            paste(self._urlPattern, self._url)
            type(Key.ENTER)
    
    
    def restart(self):
        self._app.close()
        self._app.open()
        sleep(1)

        with Region(self._app.window()):
            paste(self._urlPattern, self._url)
            type(Key.ENTER)
    
    
    def window(self):
        return self._app.window()


def waitAny(images, time=None):
    if time is None:
        time = 3
    
    for t in range(time):
        image = findBestList(images)
        if image is not None:
            return image
        else:
            sleep(1)
    else:
        return None


ButtonOk = "1540118014191.png"
ButtonOk1 = "1540132926413.png"
ButtonTake = "1540106811662.png"
ButtonTakeAll = "1540107964696.png"
ButtonBack = "1540144870598.png"
ButtonParticipate = "1540116621338.png"

MenuDailyActive = "1533463475062.png"
MenuDailyEventsActive = "1533463489206.png"
MenuFight = "1533067526354.png"