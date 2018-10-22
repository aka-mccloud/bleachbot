def doKonso(times):
    for i in range(times):
        wait("1533064132760.png")
        click()
        wait("1540107964696.png", 30)
        click()


click("1540115374519.png")


doKonso(8)
click(Pattern("1533064940424.png").targetOffset(9,0))
wait(Pattern("1540115164588.png").similar(0.75).targetOffset(50,0))
click(Pattern("1540115164588.png").similar(0.75).targetOffset(50,0))

doKonso(8)

click("1533064682568.png")
