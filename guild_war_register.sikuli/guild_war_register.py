from BleachLib import *

app = BleachApp()
app.open()

wait(MenuDailyActive, 30)
hover(MenuDailyActive)
click(MenuDailyEventsActive)

if exists("1536422308406.png"):
    click("1536422308406.png")
    wait("1536422957731.png")
    click("1536422957731.png")
