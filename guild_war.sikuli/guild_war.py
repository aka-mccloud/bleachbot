from BleachLib import *

app = BleachApp()
app.open()

wait(MenuDailyActive, 60)
hover(MenuDailyActive)
wait(MenuDailyEventsActive)
click(MenuDailyEventsActive)
click(ButtonParticipate)
wait("1539102928358.png", 5)
waitVanish("1539102928358.png", 60)
click(Pattern("1540314207146.png").targetOffset(-23,0))