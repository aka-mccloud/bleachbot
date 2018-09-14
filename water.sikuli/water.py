hover("1533067526354.png")
click("1533072169963.png")
wait(Pattern("1533504305988.png").similar(0.98).targetOffset(0,53),5)
#wait(Pattern("1535612867958.png").targetOffset(5,48),5)
click()



for i in range(15):
    wait("1533072308260.png")
    click()
    wait("1533503662767.png", 120)
    click()

wait("1533072504804.png")
click()
click(Pattern("1533072597020.png").targetOffset(30,0))
