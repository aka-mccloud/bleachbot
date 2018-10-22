import os

url = os.popen('/home/tuser/flashplayer/bleach.py').read().strip()
app = App.open('/home/tuser/flashplayer/flashplayer')

paste(Pattern("1540071070819.png").targetOffset(25,0), url)
type(Key.ENTER)


while True:
    wait("1533463475062.png", 60)
    hover()
    click("1533463489206.png")
    wait("1540116621338.png")
    click()
    wait("1535883528907.png",90)
    app.close()
    app.open()
    paste(Pattern("1540071070819.png").targetOffset(25,0), url)
    type(Key.ENTER)
