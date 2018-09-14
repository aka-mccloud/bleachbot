while True:
    wait(Pattern("1533152013124.png").similar(0.95), 60)
    #wait(Pattern("1533843844994.png").similar(0.90), 60)
    click()
    sleep(2)

    if exists("1533497076504.png"):
        click()

    if exists("1533152531028.png"):
        click()

    wait("1533152084739.png", 180)
    click()
