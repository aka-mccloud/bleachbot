hover("1533067526354.png")
click("1533147124645.png")
click(Pattern("1533153296379.png").targetOffset(0,143))
click("1533147187373.png")
if exists("1533147212357.png"):
    click("1533147212357.png")

enemies = [Pattern("1533153423955.png").similar(0.91), Pattern("1533154134699.png").similar(0.90), Pattern("1533364324030.png").similar(0.85), Pattern("1533364461405.png").similar(0.95), Pattern("1533365157615.png").similar(0.95), Pattern("1533365323672.png").similar(0.90), Pattern("1533365513591.png").similar(0.85), Pattern("1533365628048.png").similar(0.93), Pattern("1533365730144.png").similar(0.85), Pattern("1533365923200.png").similar(0.90), Pattern("1533366399641.png").similar(0.85), Pattern("1533366727985.png").similar(0.80), Pattern("1533366852426.png").similar(0.80), Pattern("1533366987314.png").similar(0.80), Pattern("1533367311555.png").similar(0.80)]

for i, enemy in enumerate(enemies):
    if exists(enemy):
        print enemy
        click(enemy)
        if i == 2 or i == 5:
            dragDrop("1533153589813.png", "1533153600716.png")
            dragDrop("1533153698332.png", "1533153600716.png")
        elif enemy == 3 or enemy == 6:
            click(Pattern("1533153743460.png").similar(0.85))
            dragDrop("1533153771268.png", "1533153782427.png")
            hover("1533364668054.png")
            dragDrop("1533153841036.png", Pattern("1533364992702.png").similar(0.85).targetOffset(0,70))
        elif i == 8:
            dragDrop("1533153589813.png", "1533153600716.png")
            dragDrop("1533153698332.png", "1533153600716.png")
            dragDrop("1533153633179.png", "1533153600716.png")
        elif i == 9:
            click(Pattern("1533153743460.png").similar(0.85))
            dragDrop("1533153771268.png", "1533153782427.png")
            hover("1533364668054.png")
            dragDrop("1533153841036.png", Pattern("1533364992702.png").similar(0.85).targetOffset(0,70))
            hover("1533364668054.png")
            dragDrop("1533366176633.png", Pattern("1533366292113.png").similar(0.85).targetOffset(0,-66))
        click("1533154038299.png")
        wait("1533147371029.png", 120)
        click("1533147371029.png")

