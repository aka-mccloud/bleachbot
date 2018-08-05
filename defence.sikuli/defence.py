while True:
    wait(Pattern("1533152013124.png").similar(0.95), 60)
    click(Pattern("1533152013124.png").similar(0.95))
    sleep(2)

    if exists("1533152031765.png"):
        click("1533152031765.png")

    if exists("1533152531028.png"):
        click("1533152531028.png")

    wait("1533152084739.png", 180)
    click("1533152084739.png")
