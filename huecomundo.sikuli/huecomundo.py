def wait_for(images, time):
    for t in range(time):
        for image in images:
            if exists(image, 0):
                return image
        else:
            sleep(1)
    else:
        return None


hover("1533067526354.png")
hover("1534061342651.png")
click("1533067560801.png")
click("1533676709589.png")
click("1540118014191.png")


stages = ["1533067606592.png", "1533067821635.png", "1533068039145.png", "1533393889163.png", "1533393901811.png", Pattern("1533393910947.png").similar(0.75), "1533393919042.png", "1533393929706.png", "1533393950242.png", "1533393960802.png", "1533393970507.png", "1533393997802.png", "1533394009466.png", "1533394019763.png", "1533394030955.png"]

for stage in stages:
    if exists(stage):
        click(stage)
        click("1533067626777.png")
        image = wait_for(["1540107964696.png", "1540132926413.png"], 120)
        if image is not None:
            if image == "1540132926413.png":
                click(image)
                break

            if image == "1540107964696.png":
                click(image)
                click("1533068223577.png")
                click("1540118014191.png")
        else:
            break

wait("1533395685525.png")
click(Pattern("1533395685525.png").targetOffset(317,1))
click("1533395758757.png")
