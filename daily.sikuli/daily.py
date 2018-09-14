game = Region(92,195,1249,650)

def salary(game):
    game.click("1536479502667.png")
    character_dialog = Region(430,313,577,430)
    character_dialog.wait("1536479541520.png")
    character_dialog.click()
    character_dialog.click(Pattern("1536479721382.png").targetOffset(15,0))


def vip(game):
    game.click("1536479944813.png")
    vip_dialog = Region(325,267,695,472)
    vip_dialog.wait("1536479994942.png")
    vip_dialog.click()
    vip_dialog.click(Pattern("1536480032614.png").targetOffset(15,0))


def shinigame_agent(game):
    game.click("1536480137615.png")
    shinigame_agent_dialog = Region(444,237,712,437)
    shinigame_agent_dialog.wait("1536480174934.png")
    shinigame_agent_dialog.click()
    if (shinigame_agent_dialog.exists("1536480174934.png")):
        shinigame_agent_dialog.click()
    shinigame_agent_dialog.click(Pattern("1536480291500.png").targetOffset(14,0))


def report(game):
    game.find("1536421696300.png")
    game.hover()
    game.find("1536480494837.png")
    game.click()

    report_dialog = Region(409,314,617,464)
    report_dialog.wait("1536480532644.png")
    report_dialog.click()
    report_dialog.click(Pattern("1536480291500.png").targetOffset(14,0))
    

def shutara_store(game):
    game.click("1536480662340.png")
    shutara_store_dialog = Region(388,304,655,432)
    shutara_store_dialog.wait("1536480735428.png")
    shutara_store_dialog.click()
    shutara_store_dialog.click(Pattern("1536480291500.png").targetOffset(14,0))


def bond(game):
    game.hover("1536481049649.png")
    game.hover("1534061342651.png")
    game.click("1536481159476.png")
    bond_dialog = Region(332,296,727,451)
    bond_dialog.click("1536481219935.png")
    bond_dialog.click("1536481265419.png")
    daily_trainig_dialog = Region(552,387,277,253)
    daily_trainig_dialog.click("1536481358572.png")
    daily_trainig_dialog.click("1536481385157.png")
    bond_dialog.click("1536481385157.png")
    

def duplicate_experience(game):
    game.hover("1536421696300.png")
    game.click("1536481554907.png")
    game.wait("1536481667205.png")
    duplicate_experience_dialog = Region(370,284,697,483)
    click(Location(719, 505))
    attack_dialog = Region(354,286,693,480)
    while attack_dialog.exists(Pattern("1536482137763.png").similar(0.95)):
        attack_dialog.click()
        report_dialog = Region(613,440,184,110)
        report_dialog.wait("1536701486041.png", 180)
        report_dialog.click()

    attack_dialog.click("1536481385157.png")
    sleep(1)
    duplicate_experience_dialog.click("1536481385157.png")
    

#salary(game)
#vip(game)
#shinigame_agent(game)
#report(game)
#shutara_store(game)
bond(game)
duplicate_experience(game)

