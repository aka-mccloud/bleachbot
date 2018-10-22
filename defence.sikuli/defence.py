from BleachLib import *

while True:
    if exists("1540063309133.png"):
        waitVanish("1540063309133.png")
    click(waitAny([Pattern("1533152013124.png").similar(0.95), Pattern("1533843844994.png").similar(0.90)], 60))
    sleep(2)

    click(waitAny(["1533497076504.png", "1533152531028.png"]))
    click(waitAny([ButtonOk1, ButtonTakeAll], 180))
