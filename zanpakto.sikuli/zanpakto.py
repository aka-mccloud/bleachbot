hover("1533067526354.png")
click("1533147124645.png")
click(Pattern("1533147154734.png").targetOffset(0,140))
click("1533147187373.png")
click("1533147212357.png")

enemies = ["1533147314572.png", "1533147429916.png", "1533147515261.png", "1533147575844.png", "1533147622981.png", "1533159833962.png", "1533147770739.png", "1533147815085.png", "1533147867388.png", "1533147912907.png", "1533147972139.png", "1533150603164.png", "1533151177484.png", "1533153081107.png", "1533153168803.png"]

for enemy in enemies:
    if exists(enemy):
        click(enemy)
        click("1533147337869.png")
        wait("1533147371029.png", 120)
        click("1533147371029.png")


click("1533153247035.png")