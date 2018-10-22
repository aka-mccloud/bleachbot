from BleachLib import BleachApp

app = BleachApp()
app.open()

with Region(app.window()):
    wait("1536421696300.png", 30)
    hover()
    click("1533463489206.png")

    if exists("1536422308406.png"):
        click()
        wait("1536422957731.png")
        click()
