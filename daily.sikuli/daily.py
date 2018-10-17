game = Region(92,195,1249,650)

def salary(game):
    game.click("1536479502667.png")
    wait("1536479541520.png")
    click()
    click(Pattern("1536479721382.png").targetOffset(15,0))


def vip(game):
    game.click("1536479944813.png")
    wait("1536479994942.png")
    click()
    click(Pattern("1536480032614.png").targetOffset(15,0))


def shinigame_agent(game):
    game.click("1536480137615.png")
    wait("1536480174934.png")
    click()
    if (exists("1536480174934.png")):
        click()
    click(Pattern("1536480291500.png").targetOffset(14,0))


def report(game):
    game.find("1536421696300.png")
    game.hover()
    game.find("1536480494837.png")
    game.click()
    game.wait("1536480532644.png")
    game.click()
    game.click(Pattern("1536480291500.png").targetOffset(14,0))
    

def shutara_store(game):
    game.click("1536480662340.png")
    game.wait("1536480735428.png")
    game.click()
    game.click(Pattern("1536480291500.png").targetOffset(14,0))


def bond(game):
    game.hover("1536481049649.png")
    game.hover("1534061342651.png")
    game.click("1536481159476.png")
    game.click("1536481219935.png")
    game.click("1536481265419.png")
    game.click("1536481358572.png")
    game.click("1536481385157.png")
    game.click("1536481385157.png")
    

def duplicate_experience(game):
    game.hover("1536421696300.png")
    game.click("1536481554907.png")
    game.wait("1536481667205.png")
    click(Location(719, 505))
    while exists(Pattern("1536482137763.png").similar(0.97)):
        click()
        wait("1536701486041.png", 180)
        click()

    click("1536481385157.png")
    sleep(1)
    click("1536481385157.png")
    

salary(game)
vip(game)
shinigame_agent(game)
report(game)
shutara_store(game)
bond(game)
duplicate_experience(game)

