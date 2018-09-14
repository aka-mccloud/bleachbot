game = Region(92,195,1249,650)

game.find("1536421696300.png")
game.hover()
game.find("1533463489206.png")
game.click()

if events_dialog.exists("1536422308406.png"):
    events_dialog.click()
    events_dialog.wait("1536424551889.png")
    events_dialog.click()

    stats = Region(1171,340,165,176)
    stats.click(Pattern("1536424621014.png").targetOffset(-21,-1))