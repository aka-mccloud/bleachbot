def waitAny(images, time=None):
    if time is None:
        time = 3
    
    for t in range(time):
        image = findBestList(images)
        if image is not None:
            return image
        else:
            sleep(1)
    else:
        return None

while True:
    click(waitAny([Pattern("1533152013124.png").similar(0.95), Pattern("1533843844994.png").similar(0.90)], 60))
    sleep(2)

    if exists("1533497076504.png"):
        click()

    if exists("1533152531028.png"):
        click()

    wait("1533152084739.png", 180)
    click()
