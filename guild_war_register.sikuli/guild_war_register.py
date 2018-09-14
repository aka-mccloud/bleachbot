game = Region(92,195,1249,650)

game.find("1536421696300.png")
game.hover()
game.find("1533463489206.png")
game.click()

events_dialog = Region(411,299,616,457)
if events_dialog.exists("1536422308406.png"):
    events_dialog.click()
    events_dialog.wait("1536422957731.png")
    events_dialog.click()
