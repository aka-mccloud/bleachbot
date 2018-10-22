from BleachLib import *

def salary():
    click("1536479502667.png")
    wait(ButtonTake)
    click()
    click(Pattern("1536479721382.png").targetOffset(15,0))


def vip():
    click("1540107098080.png")
    wait("1540107123857.png")
    click()
    click(Pattern("1536480032614.png").targetOffset(15,0))


def shinigame_agent():
    click("1540107144249.png")
    wait("1540107167504.png")
    click()
    if (exists("1540107167504.png")):
        click()
    click(Pattern("1536480291500.png").targetOffset(14,0))


def report():
    find("1536421696300.png")
    hover()
    find("1536480494837.png")
    click()
    wait("1540107201899.png")
    click()
    click(Pattern("1536480291500.png").targetOffset(14,0))
    

def shutara_store():
    click("1536480662340.png")
    wait("1540107225787.png")
    click()
    click(Pattern("1536480291500.png").targetOffset(14,0))


def bond():
    hover("1536481049649.png")
    hover("1534061342651.png")
    click("1536481159476.png")
    click("1536481219935.png")
    click("1540107288962.png")
    click("1540107315596.png")
    click("1536481385157.png")
    click("1536481385157.png")
    

def duplicate_experience():
    hover("1536421696300.png")
    click("1540108385362.png")
    wait("1540107353554.png")
    enemies = findAll("1540107476194.png")
    click(next(iter(sorted(enemies, key=lambda x: x.getX(), reverse=True))))
    while exists(Pattern("1540107712829.png").similar(0.97)):
        click()
        wait(ButtonTakeAll, 180)
        click()

    click("1536481385157.png")
    sleep(1)
    click("1536481385157.png")
    

def pet():
    click("1540188449415.png")
    wait("1540188485934.png")
    for i in range(5):
        click("1540188485934.png")
    click("1540188543177.png")
    

def homestead():
    click("1540115374519.png")
    wait("1540188784882.png")
    for i in range(13):
        click("1540188784882.png")
    click("1533064682568.png")
    

def beauty():
    click(Pattern("1540189092687.png").targetOffset(45,2))
    sleep(1)
    click("1540189134199.png")
    sleep(1)
    for i in range(5):
        click("1540189187259.png")
    click(Pattern("1536480291500.png").targetOffset(14,0))
    
    

#salary()
#vip()
#shinigame_agent()
#report()
#shutara_store()
#bond()
#duplicate_experience()
#pet()
#homestead()
beauty()