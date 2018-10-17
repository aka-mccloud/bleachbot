game = Region(92,195,1249,650)

game.find("1536421696300.png")
game.hover()
game.find("1533463489206.png")
game.click()
events_dialog = Region(411,299,616,457)

events_dialog.click("1536424551889.png")

wait("1539102928358.png", 60)
waitVanish("1539102928358.png", 60)

stats = Region(1176,347,161,175)
stats.click(Pattern("1536424621014.png").targetOffset(-21,-1))