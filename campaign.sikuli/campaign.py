from BleachLib import *

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


while True:
    sleep(1)
    click(Pattern("1533754575036.png").similar(0.80).targetOffset(0,122))
#    click(Pattern("1536007162836.png").targetOffset(0,65))
    click(waitAny(["1533754638760.png", "1533842472749.png"]))
    wait(ButtonTakeAll, 180)
    click(ButtonTakeAll)

