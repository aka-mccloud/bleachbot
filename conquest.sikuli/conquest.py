def waitAny(images, time):
    for t in range(time):
        image = findBestList(images)
        if image is not None:
            return image
        else:
            sleep(1)
    else:
        return None


def doCleanup():
    click("1540133636954.png")
    sleep(1)
    
    i = 0
    while exists(Pattern("1533754575036.png").similar(0.80).targetOffset(0,122)) and i < 3:
        click()
        click("1533842472749.png")
        wait("1540107964696.png", 180)
        click()
        i += 1


def doConquest(conquest, difficulty):
    click(conquest)
    click(difficulty)
    if exists("1540118014191.png"):
        click()
    
    doCleanup()
    
    click("1533153247035.png")
    click(Pattern("1538136983838.png").targetOffset(15,-1))


hover("1533067526354.png")
hover("1534061342651.png")
click("1533147124645.png")

conquests = [
        (Pattern("1533147154734.png").targetOffset(0,145), Pattern("1538132303896.png").similar(0.85)), 
        (Pattern("1538132636055.png").targetOffset(8,133), Pattern("1538132303896.png").similar(0.85)),
        (Pattern("1538132807630.png").targetOffset(0,134), Pattern("1538132680592.png").similar(0.80))]

for conquest in conquests:
    doConquest(*conquest)

click(Pattern("1538137875037.png").targetOffset(15,0))
