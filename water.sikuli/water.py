hover("1533067526354.png")
click("1533072169963.png")
wait("1540115941690.png", 5)
startButtons = findAll("1540115941690.png")
startButtons = sorted(startButtons, key=lambda x: x.getX())
click(startButtons[1])

for i in range(15):
    click(Pattern("1540115894036.png").similar(0.90))
    wait("1540107964696.png", 120)
    click()

wait(Pattern("1533072504804.png").targetOffset(53,0))
click()
click(Pattern("1533072597020.png").targetOffset(30,0))
