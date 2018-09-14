hover("1533067526354.png")
click("1533668065555.png")
wait("1533668090451.png")
click()
sleep(1)

click("1533668112099.png")
sleep(2)
#click(Pattern("1533841120123.png").similar(0.95))
click("1533668112099.png")
sleep(20)


for i in range(13):
    sleep(3)
    wait("1533668215827.png", 30)
    click()
    click("1533668310627.png")
    sleep(10)
    wait("1533668350717.png", 30)
    click()
    wait(Pattern("1533493272223.png").similar(0.85), 120)
    click()
